<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/compare/ac1d2409aef149089b2a89c9480844fcefaf52a3...0.1.0) (2026-11-19)

### Features

- **server:** add FastAPI application entry point ([9b02d09](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/9b02d09dbbd030eda61a2d6132b53f8cac363d6a))
- **schemas:** add validation constraints to goods fields ([8f0d3bd](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8f0d3bd05e287d93e1cc2b46604634be02ffeeb5))
- **router:** add new router module skeleton ([1b395e8](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/1b395e8f763afcd7034a06c098769ffc627fd56a))
- **routers:** initialize API routers package for FastAPI ([e48aea8](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/e48aea8bfae2d78579d15fc7b63c3455adecd766))
- **endpoints:** add API endpoints package initialization ([83ba710](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/83ba7102be8e223e581683a81b62cbe943d1fec0))
- **dbkit:** add ExecutionModes enum for sync and async operations ([e786a45](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/e786a45122498504a5256667c2ae426f1ccd8904))
- **fapi:** add async session initialization module ([08de8a4](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/08de8a43bc763195dc957149196da59748621512))
- **goods:** add goods Pydantic schemas for API ([b303a90](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/b303a908a0bf4398c8917638bed252b63e0db6c8))
- **fapi:** add async table readiness check utility ([8b86a31](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8b86a319205e9d9e3fb34e22988d5d6829fe619f))
- **dbkit:** add async engine support to InitEngine ([c0fc5be](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/c0fc5be5e9b61c0e6e4dcc01a6f411474da485e0))
- **configs:** add async mode and connection pool settings ([9dddfb8](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/9dddfb85ba39bc7cb08b526f5e9e5ae2b2e55d9a))
- **dbkit:** add BASE abstract class and new column types ([d210859](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/d2108591644713172890212cedd97ba3c7278172))
- **backend:** export BASE from dbkit module ([eecf6ca](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/eecf6ca204766855f42171623f2daed59c894204))
- **fapi:** expose core components and add package metadata ([7137953](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/7137953be31091e9e2a7d74568b16f3e0c8975b7))
- **dbkit:** export BASE and ExecutionModes from package ([b4c2557](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/b4c25577f75118a7c4e72acfab676ac152def872))
- **tools:** add DBReadyStatus enum for database state ([21233af](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/21233af8698d354f4bee999a8a0ecc6d155da625))
- **tools:** add database readiness check service ([ef42465](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/ef42465a11704ef2cce77cb13a084aadf88d2ca7))
- **dbkit:** add Goods model for product inventory ([45db325](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/45db3253909d859df6444691f4ae4f03d22cc449))
- **main:** integrate frontend modules into main entry point ([802f90d](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/802f90dddff71be77d0d9affcbc9c4d7df86ae13))
- **layout:** add page config and sidebar nav ([a51cbfe](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/a51cbfe677b5b680e74bd6c8ad6d577ab786ed0f))
- **frontend:** add SQLite database initialisation subpage ([9c44f5e](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/9c44f5ef01aef8e6c92863e804a4945b2cd8c973))
- **home:** add home subpage with runner pro introduction ([3f94136](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/3f94136272e871f2b5b94a8d4e3a174c19c8d21c))
- **dialogs:** add CRUD dialog components for data management ([7d42336](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/7d42336b0acd71b20fda28fd7d69ad6f4d0ce42e))
- **tools:** create tools package with submodule exports ([97ebf47](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/97ebf4720347fb9493a499ad4c54fef683a55e51))
- **subpages:** add __init__.py for Streamlit subpages package ([b4fcc29](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/b4fcc291fd3e95ec15a411180cbec968b5cccdbd))
- update the uv.lock file ([62dc8dc](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/62dc8dc462f831291817859e85c184617ad4baff))
- **frontend:** create initial __init__.py module skeleton ([6637ba2](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/6637ba2055ba6f758ba34f675ec61440538d3ae0))
- **network:** add module init file ([18687f9](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/18687f98660bdfc4bd78b9604260615121ccb5ea))
- **frontend:** add app module init file ([fc0875d](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/fc0875d419bd623638c2217b35751a451054d8d9))
- **backend:** add backend module initialization file ([f056e03](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/f056e0341f778361f6e7fca972de2fe1f80da81b))
- **fapi:** initialize backend fapi package ([8df758b](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8df758beed099dd0655c3015684322d754408a51))
- **dbkit:** add general column type annotations for models ([6c479aa](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/6c479aa8abc8b8be94409c8a05dfa451c4f3dba4))
- **dbkit:** add database management toolkit package ([e2467a5](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/e2467a5739d52b7c766dd80ccb78271543c5e2f4))
- **stats:** add data processing toolkit module ([fe34232](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/fe3423284fc7d48a1228c5732c2f6489f57b0031))
- **utils:** add comprehensive utility toolkit module ([10cab0e](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/10cab0e45a2014df1af5052165f83c357a716930))

### Bug Fixes

- **tools:** convert price between Decimal and float types ([f9872f1](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/f9872f1152103f8103c7910abef1b9c0942641fc))

### Chore

- **server:** remove unused imports from server module ([db17f30](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/db17f30541669148a82afe79d1bd0fb182d5a99e))
- **fapi:** add .gitignore for routers directory ([8570774](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/857077454174f963ee337f7e0f6581aa7b7cceb6))
- **endpoints:** add .gitignore for backend router directory ([3096472](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/3096472386fbf2b027674232993c4309228e4096))
- **deps:** add fastapi, greenlet, and pydantic dependencies ([a07c814](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/a07c814786a32288fda5304f05e49ed7190d6031))
- **tools:** add .gitignore for Python tools directory ([a983482](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/a9834827d553edab9f28a9010f54e37c7eee02f4))
- **subpages:** add .gitignore for Python project files ([498d0a6](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/498d0a6dbb61f8ed73f7338152961d245dc80090))
- **deps:** add streamlit and watchdog dependencies ([3d874d1](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/3d874d1eb79dae56b287c260e696c218c6f89126))
- **frontend:** add .gitignore for Python artifacts and IDE files ([6bb51c1](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/6bb51c1e410292786c8ed68b988d900218e4b133))
- **network:** add .gitignore for Python project files ([536fc47](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/536fc4787d3050d4596ea940e4669fa90dcd34b8))
- **frontend/app:** add .gitignore for Python and IDE files ([af52fa2](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/af52fa2ea02665bda62ee67ec832d2675b08bb2b))
- **fapi:** add .gitignore for fapi backend module ([c0aee4b](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/c0aee4b528eaaa1a008a5de860ed5a903d2f6c7a))
- **dbkit:** add .gitignore for backend dbkit module ([24a997c](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/24a997c3ed242fad3b23488eebe7a250d599b719))
- **deps:** add sqlalchemy as a project dependency ([8b3f9c5](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8b3f9c59a543159db636c624c33b61056bd5b6d0))
- **deps:** add sqlalchemy dependency to project ([cc5a21e](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/cc5a21e8eeaf55e7b77efafcf1414f8d65213e41))
- **changelog:** update entries with new features and deps ([7f9c8af](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/7f9c8afaf1bdeb07edc9eecaaad26df1f591a3dc))
- **deps:** update lock file with new dependencies and markers ([2c94469](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/2c94469174544229b9f7ddbaa1fdaa4faf5a7f8a))
- **deps:** add access-modifiers and pandas to dependencies ([36d211a](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/36d211aed7c659b5e574f68b42cab23c9d8f3e81))
- **changelog:** bump version to 0.1.0 and add new entries ([60a3870](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/60a3870d31887b3eb1ff65b4cace703ba5dd8cf1))
- **data:** add .gitignore for Python and IDE files ([70a49d9](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/70a49d9147f2cfd8bf6c0e15de7b6e74a36dd080))
- **deps:** add uv.lock file for dependency resolution ([77adbda](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/77adbda8d1a92dbd7edf0f6b8e1bef3a99248d9d))
- **project:** add pyproject.toml with project config ([ebd6d74](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/ebd6d7473bc016c5415477a55110611eba8409be))
- **config:** add .python-version file specifying Python 3.12 ([9fbf810](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/9fbf8109964935d4461135b875b47ad5ce3cefc3))
- **gitignore:** add .gitignore for Python projects ([a9e5ea5](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/a9e5ea51629af863068ee1edd4b3c4db57ddc111))

### Docs

- **changelog:** add entries for features and chores ([78e72f8](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/78e72f86a9ed3ad6bde6831dbb617f2ec030a02f))
- **changelog:** add entries for features and fixes ([543991b](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/543991bdf269db0e5bc1b9f7ef197b4512c3b10d))
- **changelog:** add entries for features, refactoring, and tests ([c82b93a](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/c82b93ae25236d0cb9f4aad9d0bcbffadb4003b1))
- **changelog:** add new entries for recent changes ([2c8afc9](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/2c8afc98a171b146841e5b0c701d81922c98ba20))
- **changelog:** update entries with new features and refactoring ([2996de8](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/2996de8b31461e08005556c59d1c191728b1353e))
- **changelog:** update entries with new features and deps ([55af22c](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/55af22c5b5c0133c6b504da4f994d75fb62a2c31))
- **changelog:** add entries for .gitignore and changelog creation ([8e4c1c3](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8e4c1c3a063dc8f7b631ca78ae4c036e3abd5264))
- **project:** add CHANGELOG.md with initial release notes ([7f58cf2](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/7f58cf28c94909e95a58de1594e3e15bd80035a6))
- **readme:** add Chinese version of README documentation ([c0b56af](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/c0b56af8691695b7d946de0851a5ace20aee030a))
- **readme:** add project README with privacy and setup guides ([4aab1c3](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/4aab1c33d5c4904f310057773762a124e598c80f))

### Code Refactoring

- **fapi:** remove unused ConfigDict import ([8caffce](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/8caffce7dc6bbdafd59401556801c7e380cc437f))
- **session:** specify session class explicitly ([0bae9ec](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/0bae9ecdcdaa4e33974f20c6188ed611caea8e05))
- **dbkit:** update Goods model to use BASE ([c72c78f](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/c72c78febfd27f6ad8197a5d66b9169bd2cc36a0))
- **dbkit:** rename repository functions for clarity ([982f0b6](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/982f0b67a50bb54d91933fc1b29a42853c43ae82))
- **dbkit:** drop context manager support ([4ca2c07](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/4ca2c070cfbcb5ccd62ca0c29f7531e3b54835b1))
- **dbkit:** rename BASE constant to BASE_DIR for clarity ([86eb651](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/86eb651a5bb8a94f0e93fa2e40a369601595dbce))
- **dbkit:** split NUM into specific typed column annotations ([19a8116](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/19a8116bb23e2de410f9058086cb705019624529))
- **frontend:** restructure __init__ as package interface ([674b73e](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/674b73e0aa6d879a3ad3fa54fb4b87650c60fbb5))
- **app:** restructure __init__.py as proper package module ([4b4807d](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/4b4807d3b7350f1cd959eb4642e6c0e9400d0392))
- **backend:** expose dbkit API in package init ([ed53068](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/ed53068add8ac0d4abf47252cc1cad386a537563))
- **dbkit:** rename repository functions and export Goods model ([71bab4a](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/71bab4a1df9c0a7afc8abab0289df66fa613806c))
- **dbkit:** move dbkit module from utils to backend ([46ca088](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/46ca088cd73b40bc890c5ad6943ef2071ce7021c))
- **dbkit:** remove GENERAL column type definitions ([f0ffac3](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/f0ffac3b18ccb907e6d34e71de5c3164e5552c6e))

### Tests

- **backend:** add integration test for database module lifecycle ([99e7621](https://github.com/DaoChaShao/py-st-vintage-good-retrader-langgraph/commit/99e7621d2d23cc0356e3f4b6f4e3a60d59f0a2e8))
