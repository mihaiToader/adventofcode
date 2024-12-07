import { memo, useEffect, useMemo, useRef, useState } from 'react';


const getTileColor = (value) => {
    if (value === '.') {
        return 'gray'
    }
    if (value === 'X') {
        return 'green'
    }
    if (value === '#') {
        return 'red'
    }
    if (value === '0') {
        return 'blue'
    }
    if (value === '^') {
        return 'yellow'
    }
    if (value === 'L') {
        return '#0b4011'
    }
}

const Tile = memo(({i, j, value}) => {
    const randomColor = getTileColor(value);
    return (
        <div className='w-3 h-3 border-solid border border-black' style={{backgroundColor: randomColor}}/>
    )
});

const SIMULATION_MS = 500;

const Map = () => {
    const map = useRef(null);
    const patrol = useRef(null);
    const patrolIndex = useRef(null);
    const patrolMapRef = useRef(null);
    const speedRef = useRef(SIMULATION_MS);
    const [speed, setSpeed] = useState(SIMULATION_MS);
    const [patrolMap, setPatrolMap] = useState(null);
    const [loops, setLoops] = useState(null);
    const [loopCounter, setLoopCounter] = useState(0);

    useEffect(() => {
        fetch('http://localhost:3000/patrol/').then(res => res.json()).then(data => {
            setPatrolMap(data.map);
            patrolMapRef.current = structuredClone(data.map);
            map.current = structuredClone(data.map);
            patrol.current = data.patrol;
            setLoops(data.loops);
        })
    }, []);

    const mapTiles = useMemo(() => {
        if (!patrolMap) {
            return null;
        }
        const tiles = []
        for (let i = 0; i < patrolMap.length; i++) {
            for (let j = 0; j < patrolMap[0].length; j++) {
                tiles.push(
                    <Tile i={i} j={j} value={patrolMap[i][j]} key={`${i}-${j}-${patrolMap[i][j]}`}/>
                )
            }
        }
        return tiles
    }, [patrolMap]);

    const requestRef = useRef();
    const previousTimeRef = useRef();

    const simulatePatrol = () => {
        if (!patrolIndex.current) {
            patrolIndex.current = 0;
        }

        if (patrolIndex.current >= patrol.current.length - 2) {
            return false;
        }

        const currentPositionCoord = patrol.current[patrolIndex.current]
        patrolIndex.current += 1;

        const newPositionCoord = patrol.current[patrolIndex.current]

        patrolMapRef.current[currentPositionCoord[0]][currentPositionCoord[1]] = 'X'
        patrolMapRef.current[newPositionCoord[0]][newPositionCoord[1]] = '^'
        setPatrolMap(structuredClone(patrolMapRef.current))
        return true;
    }

    const animate = now => {
        if (!previousTimeRef.current || now - previousTimeRef.current >= speedRef.current) {
            previousTimeRef.current = now;
            const isRunning = simulatePatrol()
            if (!isRunning) {
                cancelAnimationFrame(requestRef.current);
                return;
            }
        }
        requestRef.current = requestAnimationFrame(animate);
    }


    const startSimulation = () => {
        requestRef.current = requestAnimationFrame(animate);
    }

    const reset = () => {
        cancelAnimationFrame(requestRef.current);
        patrolIndex.current = 0;
        patrolMapRef.current = structuredClone(map.current);
        setPatrolMap(structuredClone(map.current))
    }

    const pauseSimulation = () => {
        cancelAnimationFrame(requestRef.current);
    }

    const onChangeSpeed = (event) => {
        setSpeed(event.target.value);
        speedRef.current = event.target.value;
    }

    const goToEnd = () => {
        reset();
        while (simulatePatrol()) {
        }
    }

    const onChangeLoop = (event) => {
        setLoopCounter(event.target.value)
    }

    const showLoop = () => {
        reset();
        const loop = loops[loopCounter]

        const patrol = structuredClone(loop.patrol)
        const obstacle = loop.obstacle;

        patrolMapRef.current[obstacle[0]][obstacle[1]] = '0'

        const endOfLoopCoord = patrol[patrol.length - 1]

        let patrolIndex = 0;
        let isInLoop = false;
        while (patrolIndex < patrol.length) {
            const currentCord = patrol[patrolIndex]
            if (!isInLoop && currentCord[0] === endOfLoopCoord[0] && currentCord[1] === endOfLoopCoord[1]) {
                isInLoop = !isInLoop;
            }
            if (isInLoop) {
                patrolMapRef.current[currentCord[0]][currentCord[1]] = 'L'
            } else {
                patrolMapRef.current[currentCord[0]][currentCord[1]] = 'X'
            }
            patrolIndex += 1
        }

        setPatrolMap(structuredClone(patrolMapRef.current))
    }

    if (!patrolMap) {
        return null;
    }

    return (
        <div>
            <div className='flex mt-2 mb-2'>
                <button
                    className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2"
                    type="button" onClick={startSimulation}>
                    Start
                </button>
                <button
                    className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2"
                    type="button" onClick={pauseSimulation}>
                    Pause
                </button>
                <button
                    className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2"
                    type="button" onClick={reset}>
                    Reset
                </button>
                <div className="relative w-100 ml-4">
                    <label htmlFor="small-range"
                           className="absolute block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                           style={{top: '-10px'}}>{speed} ms</label>
                    <input id="small-range" type="range" value={speed} onChange={onChangeSpeed} min={0} max={1250}
                           className="w-full h-1 mb-6 bg-gray-200 rounded-lg appearance-none cursor-pointer range-sm dark:bg-gray-700"/>
                </div>
                <button
                    className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2"
                    type="button" onClick={goToEnd}>
                    Go to End
                </button>
                {!!loops && (
                    <>
                        <div className="relative w-20 ml-4">
                            <input type="number" value={loopCounter} onChange={onChangeLoop} max={loops.length - 1}
                                   min={0}
                                   className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            />
                        </div>
                        <button
                            className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none ml-2"
                            type="button" onClick={showLoop}>
                            Show Loop
                        </button>
                    </>
                )}
            </div>
            <div className='grid'
                 style={{gridTemplateColumns: `repeat(${patrolMap[0].length}, 12px [col-start])`}}>
                {mapTiles}
            </div>
        </div>
    )
}

export default Map;
