import express from 'express';
import fs from 'node:fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import cors from 'cors';

const app = express()
const port = 3000

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(cors())

const parseLoops = (loops) => {
    if (!loops) {
        return null;
    }
    return loops.split('\n').filter(l => l.length > 0).map(loop => loop.split(',').map(coor => coor.split('|').map(v => +v))).map(loop => ({
        obstacle: loop[0],
        patrol: loop.slice(1)
    }))
}

const parseData = (data) => {
    const [map, patrol, loops] = data.split('-\n');

    return {
        map: map.split('\n').map(row => row.split('')).filter(row => row.length > 0),
        patrol: patrol ? patrol.split(',').map(coor => coor.split('|').map(v => +v)): null,
        loops: parseLoops(loops)
    }
}
app.get('/patrol/', async (req, res) => {
    const filePath = path.join(__dirname, '../../output', `patrol.txt`);

    try {
        const data = await fs.readFile(filePath, {encoding: 'utf8'});
        res.json(parseData(data))
        return;
    } catch (err) {
        console.log(err);
    }
    res.json({code: 'Something went wrong!'}).status(500);
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})