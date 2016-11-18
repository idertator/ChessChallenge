# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.1.1] - 2016-11-18

### Added
- In the RecursiveBruteForceSolver skips to check solutions if the current
piece is the same than previous and starts and have the same available slots.

### Changed

- In the RecursiveBruteForceSolver replaced the set of integers as visited 
configuration check for it's hash. This reduce dramatically the memory
footprint of the algorithm.

- In the RecursiveBruteForceSolver store only visited configurations with
2 to 5 pieces. This reduce the memory footprint of the algorithm.
