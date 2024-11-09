import { bench, run } from 'mitata';
import { myRandom } from './index';

bench('myRandom', () => {
  myRandom();
});

run();