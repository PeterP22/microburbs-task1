import React from 'react';
import {Composition} from 'remotion';
import {Task1Reel} from './task1/Task1Reel';
import task1 from '../data/task1.json';
export const RemotionRoot:React.FC=()=> <Composition id="Task1Reel" component={Task1Reel} durationInFrames={900} fps={30} width={1080} height={1920} defaultProps={task1}/>;
