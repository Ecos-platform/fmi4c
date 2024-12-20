import ctypes as ct

class fmi4c:

    class fmi1EventInfo(ct.Structure):
        _fields_=[("upcomingTimeEvent",ct.c_bool),
              ("stateValuesChanged",ct.c_bool),
              ("terminateSimulation",ct.c_bool),
              ("iterationConverged",ct.c_bool),
              ("nextEventTime",ct.c_double)]

    def __init__(self):
        import ctypes
        import os
        if os.name == "posix":
            self.hdll = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.abspath(__file__)) + "/../libfmi4c.so")
        elif os.name == "nt":
            self.hdll = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.abspath(__file__)) + "/../libfmi4c.dll")
        self.hdll.fmi4c_getFmiVersion.restype = ct.c_int
        self.hdll.fmi4c_getFmiVersion.argtypes = ct.c_void_p,
        self.hdll.fmi4c_loadFmu.restype = ct.c_void_p
        self.hdll.fmi4c_loadFmu.argtypes = ct.c_char_p, ct.c_char_p,
        self.hdll.fmi4c_freeFmu.restype = None
        self.hdll.fmi4c_freeFmu.argtypes = ct.c_void_p,
        
        #FMI1 metadata functions
        self.hdll.fmi1_getType.restype = ct.c_int
        self.hdll.fmi1_getType.argtypes = ct.c_void_p,
        self.hdll.fmi1_getModelName.restype = ct.c_char_p
        self.hdll.fmi1_getModelName.argtypes = ct.c_void_p,
        self.hdll.fmi1_getModelIdentifier.restype = ct.c_char_p
        self.hdll.fmi1_getModelIdentifier.argtypes = ct.c_void_p,
        self.hdll.fmi1_getGuid.restype = ct.c_char_p
        self.hdll.fmi1_getGuid.argtypes = ct.c_void_p,
        self.hdll.fmi1_getDescription.restype = ct.c_char_p
        self.hdll.fmi1_getDescription.argtypes = ct.c_void_p,
        self.hdll.fmi1_getAuthor.restype = ct.c_char_p
        self.hdll.fmi1_getAuthor.argtypes = ct.c_void_p,
        self.hdll.fmi1_getGenerationTool.restype = ct.c_char_p
        self.hdll.fmi1_getGenerationTool.argtypes = ct.c_void_p,
        self.hdll.fmi1_getGenerationDateAndTime.restype = ct.c_char_p
        self.hdll.fmi1_getGenerationDateAndTime.argtypes = ct.c_void_p,
        self.hdll.fmi1_getNumberOfContinuousStates.restype = ct.c_int
        self.hdll.fmi1_getNumberOfContinuousStates.argtypes = ct.c_void_p,
        self.hdll.fmi1_getNumberOfEventIndicators.restype = ct.c_int
        self.hdll.fmi1_getNumberOfEventIndicators.argtypes = ct.c_void_p,
        self.hdll.fmi1_defaultStartTimeDefined.restype = ct.c_bool
        self.hdll.fmi1_defaultStartTimeDefined.argtypes = ct.c_void_p,
        self.hdll.fmi1_defaultStopTimeDefined.restype = ct.c_bool
        self.hdll.fmi1_defaultStopTimeDefined.argtypes = ct.c_void_p,
        self.hdll.fmi1_defaultToleranceDefined.restype = ct.c_bool
        self.hdll.fmi1_defaultToleranceDefined.argtypes = ct.c_void_p,
        self.hdll.fmi1_getDefaultStartTime.restype = ct.c_double
        self.hdll.fmi1_getDefaultStartTime.argtypes = ct.c_void_p,
        self.hdll.fmi1_getDefaultStopTime.restype = ct.c_double
        self.hdll.fmi1_getDefaultStopTime.argtypes = ct.c_void_p,
        self.hdll.fmi1_getDefaultTolerance.restype = ct.c_double
        self.hdll.fmi1_getDefaultTolerance.argtypes = ct.c_void_p,
        self.hdll.fmi1_getNumberOfVariables.restype = ct.c_int
        self.hdll.fmi1_getNumberOfVariables.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableByIndex.restype = ct.c_void_p
        self.hdll.fmi1_getVariableByIndex.argtypes = ct.c_void_p,ct.c_int
        self.hdll.fmi1_getVariableByValueReference.restype = ct.c_void_p
        self.hdll.fmi1_getVariableByValueReference.argtypes = ct.c_void_p,ct.c_int
        self.hdll.fmi1_getVariableByName.restype = ct.c_void_p
        self.hdll.fmi1_getVariableByName.argtypes = ct.c_void_p,ct.c_char_p
        self.hdll.fmi1_getVariableName.restype = ct.c_char_p
        self.hdll.fmi1_getVariableName.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableDescription.restype = ct.c_char_p
        self.hdll.fmi1_getVariableDescription.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableQuantity.restype = ct.c_char_p
        self.hdll.fmi1_getVariableQuantity.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableUnit.restype = ct.c_char_p
        self.hdll.fmi1_getVariableUnit.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableDisplayUnit.restype = ct.c_char_p
        self.hdll.fmi1_getVariableDisplayUnit.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableRelativeQuantity.restype = ct.c_bool
        self.hdll.fmi1_getVariableRelativeQuantity.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableMin.restype = ct.c_double
        self.hdll.fmi1_getVariableMin.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableMax.restype = ct.c_double
        self.hdll.fmi1_getVariableMax.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableNominal.restype = ct.c_double
        self.hdll.fmi1_getVariableNominal.argtypes = ct.c_void_p,
        self.hdll.fmi1_getNumberOfBaseUnits.restype = ct.c_int
        self.hdll.fmi1_getNumberOfBaseUnits.argtypes = ct.c_void_p,
        self.hdll.fmi1_getBaseUnitByIndex.restype = ct.c_void_p
        self.hdll.fmi1_getBaseUnitByIndex.argtypes = ct.c_void_p,ct.c_int,
        self.hdll.fmi1_getBaseUnitUnit.restype = ct.c_char_p
        self.hdll.fmi1_getBaseUnitUnit.argtypes = ct.c_void_p,
        self.hdll.fmi1_getNumberOfDisplayUnits.restype = ct.c_int
        self.hdll.fmi1_getNumberOfDisplayUnits.argtypes = ct.c_void_p,
        self.hdll.fmi1_getDisplayUnitByIndex.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_char_p),ct.POINTER(ct.c_double),ct.POINTER(ct.c_double),
        self.hdll.fmi1_getVariableHasStartValue.restype = ct.c_bool
        self.hdll.fmi1_getVariableHasStartValue.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableStartReal.restype = ct.c_double
        self.hdll.fmi1_getVariableStartReal.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableStartInteger.restype = ct.c_int
        self.hdll.fmi1_getVariableStartInteger.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableStartBoolean.restype = ct.c_bool
        self.hdll.fmi1_getVariableStartBoolean.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableStartString.restype = ct.c_char_p
        self.hdll.fmi1_getVariableStartString.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableValueReference.restype = ct.c_uint
        self.hdll.fmi1_getVariableValueReference.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableCausality.restype = ct.c_int
        self.hdll.fmi1_getVariableCausality.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableVariability.restype = ct.c_int
        self.hdll.fmi1_getVariableVariability.argtypes = ct.c_void_p,
        self.hdll.fmi1_getAlias.restype = ct.c_int
        self.hdll.fmi1_getAlias.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableIsFixed.restype = ct.c_bool
        self.hdll.fmi1_getVariableIsFixed.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVariableDataType.restype = ct.c_int
        self.hdll.fmi1_getVariableDataType.argtypes = ct.c_void_p,

        #FMI1 functions
        self.hdll.fmi1_getTypesPlatform.restype = ct.c_char_p
        self.hdll.fmi1_getTypesPlatform.argtypes = ct.c_void_p,
        self.hdll.fmi1_getVersion.restype = ct.c_char_p
        self.hdll.fmi1_getVersion.argtypes = ct.c_void_p,
        self.hdll.fmi1_setDebugLogging.restype = ct.c_int
        self.hdll.fmi1_setDebugLogging.argtypes = ct.c_void_p,ct.c_bool,
        self.hdll.fmi1_getReal.restype = ct.c_int
        self.hdll.fmi1_getReal.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_double),
        self.hdll.fmi1_getInteger.restype = ct.c_int
        self.hdll.fmi1_getInteger.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),
        self.hdll.fmi1_getBoolean.restype = ct.c_int
        self.hdll.fmi1_getBoolean.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_bool),
        self.hdll.fmi1_getString.restype = ct.c_int
        self.hdll.fmi1_getString.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_char_p),
        self.hdll.fmi1_setReal.restype = ct.c_int
        self.hdll.fmi1_setReal.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_double),
        self.hdll.fmi1_setInteger.restype = ct.c_int
        self.hdll.fmi1_setInteger.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),
        self.hdll.fmi1_setBoolean.restype = ct.c_int
        self.hdll.fmi1_setBoolean.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_bool),
        self.hdll.fmi1_setString.restype = ct.c_int
        self.hdll.fmi1_setString.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_char_p),
        self.hdll.fmi1_instantiateSlave.restype = ct.c_bool
        self.hdll.fmi1_instantiateSlave.argtypes = ct.c_void_p,ct.c_char_p,ct.c_double,ct.c_bool,ct.c_bool,ct.c_void_p,ct.c_void_p,ct.c_void_p,ct.c_void_p, ct.c_bool,
        self.hdll.fmi1_initializeSlave.restype = ct.c_int
        self.hdll.fmi1_initializeSlave.argtypes = ct.c_void_p,ct.c_double,ct.c_bool,ct.c_double,
        self.hdll.fmi1_terminateSlave.restype = ct.c_int
        self.hdll.fmi1_terminateSlave.argtypes = ct.c_void_p,
        self.hdll.fmi1_resetSlave.restype = ct.c_int
        self.hdll.fmi1_resetSlave.argtypes = ct.c_void_p,
        self.hdll.fmi1_freeSlaveInstance.restype = None
        self.hdll.fmi1_freeSlaveInstance.argtypes = ct.c_void_p,
        self.hdll.fmi1_setRealInputDerivatives.restype = ct.c_int
        self.hdll.fmi1_setRealInputDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),ct.POINTER(ct.c_double),
        self.hdll.fmi1_getRealOutputDerivatives.restype = ct.c_int
        self.hdll.fmi1_getRealOutputDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),ct.POINTER(ct.c_double),
        self.hdll.fmi1_cancelStep.restype = ct.c_int
        self.hdll.fmi1_cancelStep.argtypes = ct.c_void_p,
        self.hdll.fmi1_doStep.restype = ct.c_int
        self.hdll.fmi1_doStep.argtypes = ct.c_void_p,ct.c_double,ct.c_double,ct.c_bool,
        self.hdll.fmi1_getStatus.restype = ct.c_int
        self.hdll.fmi1_getStatus.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_int),
        self.hdll.fmi1_getRealStatus.restype = ct.c_int
        self.hdll.fmi1_getRealStatus.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_double),
        self.hdll.fmi1_getIntegerStatus.restype = ct.c_int
        self.hdll.fmi1_getIntegerStatus.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_int),
        self.hdll.fmi1_getBooleanStatus.restype = ct.c_int
        self.hdll.fmi1_getBooleanStatus.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_bool),
        self.hdll.fmi1_getStringStatus.restype = ct.c_int
        self.hdll.fmi1_getStringStatus.argtypes = ct.c_void_p,ct.c_int,ct.POINTER(ct.c_char_p),
        self.hdll.fmi1_getModelTypesPlatform.restype = ct.c_char_p
        self.hdll.fmi1_getModelTypesPlatform.argtypes = ct.c_void_p,
        self.hdll.fmi1_instantiateModel.restype = ct.c_bool
        self.hdll.fmi1_instantiateModel.argtypes = ct.c_void_p,ct.c_void_p,ct.c_void_p,ct.c_bool,
        self.hdll.fmi1_freeModelInstance.restype = None
        self.hdll.fmi1_freeModelInstance.argtypes = ct.c_void_p,
        self.hdll.fmi1_setTime.restype = ct.c_int
        self.hdll.fmi1_setTime.argtypes = ct.c_void_p,ct.c_double,
        self.hdll.fmi1_setContinuousStates.restype = ct.c_int
        self.hdll.fmi1_setContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,
        self.hdll.fmi1_completedIntegratorStep.restype = ct.c_int
        self.hdll.fmi1_completedIntegratorStep.argtypes = ct.c_void_p,ct.c_bool,
        self.hdll.fmi1_initialize.restype = ct.c_int
        self.hdll.fmi1_initialize.argtypes = ct.c_void_p,ct.c_bool,ct.c_double,ct.POINTER(self.fmi1EventInfo),
        self.hdll.fmi1_getDerivatives.restype = ct.c_int
        self.hdll.fmi1_getDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_int,
        self.hdll.fmi1_getEventIndicators.restype = ct.c_int
        self.hdll.fmi1_getEventIndicators.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_int,
        self.hdll.fmi1_eventUpdate.restype = ct.c_int
        self.hdll.fmi1_eventUpdate.argtypes = ct.c_void_p,ct.c_bool,ct.c_void_p,
        self.hdll.fmi1_getContinuousStates.restype = ct.c_int
        self.hdll.fmi1_getContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_int,
        self.hdll.fmi1_getNominalContinuousStates.restype = ct.c_int
        self.hdll.fmi1_getNominalContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_int,
        self.hdll.fmi1_getStateValueReferences.restype = ct.c_int
        self.hdll.fmi1_getStateValueReferences.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_int,
        self.hdll.fmi1_terminate.restype = ct.c_int
        self.hdll.fmi1_terminate.argtypes = ct.c_void_p,

        self.hdll.fmi2_defaultStartTimeDefined.restype = ct.c_bool
        self.hdll.fmi2_defaultStartTimeDefined.argtypes =ct.c_void_p,
        self.hdll.fmi2_defaultStopTimeDefined.restype = ct.c_bool
        self.hdll.fmi2_defaultStopTimeDefined.argtypes =ct.c_void_p,
        self.hdll.fmi2_defaultToleranceDefined.restype = ct.c_bool
        self.hdll.fmi2_defaultToleranceDefined.argtypes =ct.c_void_p,
        self.hdll.fmi2_defaultStepSizeDefined.restype = ct.c_bool
        self.hdll.fmi2_defaultStepSizeDefined.argtypes =ct.c_void_p,
        self.hdll.fmi2_getDefaultStartTime.restype = ct.c_double
        self.hdll.fmi2_getDefaultStartTime.argtypes =ct.c_void_p,
        self.hdll.fmi2_getDefaultStopTime.restype = ct.c_double
        self.hdll.fmi2_getDefaultStopTime.argtypes =ct.c_void_p,
        self.hdll.fmi2_getDefaultTolerance.restype = ct.c_double
        self.hdll.fmi2_getDefaultTolerance.argtypes =ct.c_void_p,
        self.hdll.fmi2_getDefaultStepSize.restype = ct.c_double
        self.hdll.fmi2_getDefaultStepSize.argtypes =ct.c_void_p,

        self.hdll.fmi2_getNumberOfVariables.restype = ct.c_int
        self.hdll.fmi2_getNumberOfVariables.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableByIndex.restype =ct.c_void_p
        self.hdll.fmi2_getVariableByIndex.argtypes =ct.c_void_p,ct.c_int,
        self.hdll.fmi2_getVariableByValueReference.restype =ct.c_void_p
        self.hdll.fmi2_getVariableByValueReference.argtypes =ct.c_void_p, ct.c_long,
        self.hdll.fmi2_getVariableByName.restype =ct.c_void_p
        self.hdll.fmi2_getVariableByName.argtypes =ct.c_void_p, ct.c_char_p,
        self.hdll.fmi2_getVariableName.restype = ct.c_char_p
        self.hdll.fmi2_getVariableName.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableDescription.restype = ct.c_char_p
        self.hdll.fmi2_getVariableDescription.argtypes = ct.c_void_p,
        self.hdll.fmi2_getFmiVersion.restype = ct.c_char_p
        self.hdll.fmi2_getFmiVersion.argtypes = ct.c_void_p,
        self.hdll.fmi2_getAuthor.restype = ct.c_char_p
        self.hdll.fmi2_getAuthor.argtypes =ct.c_void_p,
        self.hdll.fmi2_getModelName.restype = ct.c_char_p
        self.hdll.fmi2_getModelName.argtypes =ct.c_void_p,
        self.hdll.fmi2_getModelDescription.restype = ct.c_char_p
        self.hdll.fmi2_getModelDescription.argtypes =ct.c_void_p,
        self.hdll.fmi2_getCopyright.restype = ct.c_char_p
        self.hdll.fmi2_getCopyright.argtypes =ct.c_void_p,
        self.hdll.fmi2_getLicense.restype = ct.c_char_p
        self.hdll.fmi2_getLicense.argtypes =ct.c_void_p,
        self.hdll.fmi2_getGenerationTool.restype = ct.c_char_p
        self.hdll.fmi2_getGenerationTool.argtypes =ct.c_void_p,
        self.hdll.fmi2_getGenerationDateAndTime.restype = ct.c_char_p
        self.hdll.fmi2_getGenerationDateAndTime.argtypes =ct.c_void_p,
        self.hdll.fmi2_getVariableNamingConvention.restype = ct.c_char_p
        self.hdll.fmi2_getVariableNamingConvention.argtypes =ct.c_void_p,
        self.hdll.fmi2_getVariableDerivativeIndex.restype = ct.c_int
        self.hdll.fmi2_getVariableDerivativeIndex.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableQuantity.restype = ct.c_char_p
        self.hdll.fmi2_getVariableQuantity.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableUnit.restype = ct.c_char_p
        self.hdll.fmi2_getVariableUnit.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableDisplayUnit.restype = ct.c_char_p
        self.hdll.fmi2_getVariableDisplayUnit.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableRelativeQuantity.restype = ct.c_bool
        self.hdll.fmi2_getVariableRelativeQuantity.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableMin.restype = ct.c_double
        self.hdll.fmi2_getVariableMin.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableMax.restype = ct.c_double
        self.hdll.fmi2_getVariableMax.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableNominal.restype = ct.c_double
        self.hdll.fmi2_getVariableNominal.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableUnbounded.restype = ct.c_bool
        self.hdll.fmi2_getVariableUnbounded.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableHasStartValue.restype = ct.c_bool
        self.hdll.fmi2_getVariableHasStartValue.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableStartReal.restype = ct.c_double
        self.hdll.fmi2_getVariableStartReal.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableStartInteger.restype = ct.c_int
        self.hdll.fmi2_getVariableStartInteger.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableStartBoolean.restype = ct.c_bool
        self.hdll.fmi2_getVariableStartBoolean.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableStartString.restype = ct.c_char_p
        self.hdll.fmi2_getVariableStartString.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableValueReference.restype = ct.c_long
        self.hdll.fmi2_getVariableValueReference.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableCausality.restype = ct.c_int
        self.hdll.fmi2_getVariableCausality.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableVariability.restype = ct.c_int
        self.hdll.fmi2_getVariableVariability.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableInitial.restype = ct.c_int
        self.hdll.fmi2_getVariableInitial.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableCanHandleMultipleSetPerTimeInstant.restype = ct.c_bool
        self.hdll.fmi2_getVariableCanHandleMultipleSetPerTimeInstant.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVariableDataType.restype = ct.c_int
        self.hdll.fmi2_getVariableDataType.argtypes = ct.c_void_p,

        self.hdll.fmi2_getTypesPlatform.restype = ct.c_char_p
        self.hdll.fmi2_getTypesPlatform.argtypes = ct.c_void_p,
        self.hdll.fmi2_getVersion.restype = ct.c_char_p
        self.hdll.fmi2_getVersion.argtypes = ct.c_void_p,
        self.hdll.fmi2_setDebugLogging.restype = ct.c_int
        self.hdll.fmi2_setDebugLogging.argtypes = ct.c_void_p, ct.c_bool, ct.c_size_t, ct.c_char_p
        self.hdll.fmi2_getGuid.restype = ct.c_char_p
        self.hdll.fmi2_getGuid.argtypes =ct.c_void_p,

        self.hdll.fmi2cs_getModelIdentifier.restype = ct.c_char_p
        self.hdll.fmi2cs_getModelIdentifier.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanHandleVariableCommunicationStepSize.restype = ct.c_bool
        self.hdll.fmi2cs_getCanHandleVariableCommunicationStepSize.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanInterpolateInputs.restype = ct.c_bool
        self.hdll.fmi2cs_getCanInterpolateInputs.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getMaxOutputDerivativeOrder.restype = ct.c_int
        self.hdll.fmi2cs_getMaxOutputDerivativeOrder.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanRunAsynchronuously.restype = ct.c_bool
        self.hdll.fmi2cs_getCanRunAsynchronuously.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getNeedsExecutionTool.restype = ct.c_bool
        self.hdll.fmi2cs_getNeedsExecutionTool.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanBeInstantiatedOnlyOncePerProcess.restype = ct.c_bool
        self.hdll.fmi2cs_getCanBeInstantiatedOnlyOncePerProcess.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanNotUseMemoryManagementFunctions.restype = ct.c_bool
        self.hdll.fmi2cs_getCanNotUseMemoryManagementFunctions.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanGetAndSetFMUState.restype = ct.c_bool
        self.hdll.fmi2cs_getCanGetAndSetFMUState.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getCanSerializeFMUState.restype = ct.c_bool
        self.hdll.fmi2cs_getCanSerializeFMUState.argtypes = ct.c_void_p,
        self.hdll.fmi2cs_getProvidesDirectionalDerivative.restype = ct.c_bool
        self.hdll.fmi2cs_getProvidesDirectionalDerivative.argtypes = ct.c_void_p,

        self.hdll.fmi2me_getModelIdentifier.restype = ct.c_char_p
        self.hdll.fmi2me_getModelIdentifier.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getCompletedIntegratorStepNotNeeded.restype = ct.c_bool
        self.hdll.fmi2me_getCompletedIntegratorStepNotNeeded.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getNeedsExecutionTool.restype = ct.c_bool
        self.hdll.fmi2me_getNeedsExecutionTool.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getCanBeInstantiatedOnlyOncePerProcess.restype = ct.c_bool
        self.hdll.fmi2me_getCanBeInstantiatedOnlyOncePerProcess.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getCanNotUseMemoryManagementFunctions.restype = ct.c_bool
        self.hdll.fmi2me_getCanNotUseMemoryManagementFunctions.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getCanGetAndSetFMUState.restype = ct.c_bool
        self.hdll.fmi2me_getCanGetAndSetFMUState.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getCanSerializeFMUState.restype = ct.c_bool
        self.hdll.fmi2me_getCanSerializeFMUState.argtypes = ct.c_void_p,
        self.hdll.fmi2me_getProvidesDirectionalDerivative.restype = ct.c_bool
        self.hdll.fmi2me_getProvidesDirectionalDerivative.argtypes = ct.c_void_p,

        self.hdll.fmi2_getNumberOfContinuousStates.restype = ct.c_int
        self.hdll.fmi2_getNumberOfContinuousStates.argtypes =ct.c_void_p,
        self.hdll.fmi2_getNumberOfEventIndicators.restype = ct.c_int
        self.hdll.fmi2_getNumberOfEventIndicators.argtypes =ct.c_void_p,
        self.hdll.fmi2_getSupportsCoSimulation.restype = ct.c_bool
        self.hdll.fmi2_getSupportsCoSimulation.argtypes =ct.c_void_p,
        self.hdll.fmi2_getSupportsModelExchange.restype = ct.c_bool
        self.hdll.fmi2_getSupportsModelExchange.argtypes =ct.c_void_p,

        self.hdll.fmi2_instantiate.restype = ct.c_bool
        self.hdll.fmi2_instantiate.argtypes =ct.c_void_p, ct.c_int, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_void_p, ct.c_bool, ct.c_bool,
        self.hdll.fmi2_freeInstance.restype = None
        self.hdll.fmi2_freeInstance.argtypes = ct.c_void_p,

        self.hdll.fmi2_setupExperiment.restype = ct.c_int
        self.hdll.fmi2_setupExperiment.argtypes = ct.c_void_p, ct.c_bool, ct.c_double, ct.c_double, ct.c_bool, ct.c_double,
        self.hdll.fmi2_enterInitializationMode.restype = ct.c_int
        self.hdll.fmi2_enterInitializationMode.argtypes = ct.c_void_p,
        self.hdll.fmi2_exitInitializationMode.restype = ct.c_int
        self.hdll.fmi2_exitInitializationMode.argtypes = ct.c_void_p,
        self.hdll.fmi2_terminate.restype = ct.c_int
        self.hdll.fmi2_terminate.argtypes = ct.c_void_p,
        self.hdll.fmi2_reset.restype = ct.c_int
        self.hdll.fmi2_reset.argtypes = ct.c_void_p,

        self.hdll.fmi2_getNumberOfUnits.restype = ct.c_int
        self.hdll.fmi2_getNumberOfUnits.argtypes =ct.c_void_p,

        self.hdll.fmi2_getUnitByIndex.restype = ct.c_void_p
        self.hdll.fmi2_getUnitByIndex.argtypes = ct.c_void_p, ct.c_int,
        self.hdll.fmi2_getUnitName.restype = ct.c_char_p
        self.hdll.fmi2_getUnitName.argtypes = ct.c_void_p,
        self.hdll.fmi2_hasBaseUnit.restype = ct.c_bool
        self.hdll.fmi2_hasBaseUnit.argtypes = ct.c_void_p,
        self.hdll.fmi2_getBaseUnit.restype = None
        self.hdll.fmi2_getBaseUnit.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.POINTER(ct.c_double),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),ct.POINTER(ct.c_int),
        self.hdll.fmi2_getNumberOfDisplayUnits.restype = ct.c_int
        self.hdll.fmi2_getNumberOfDisplayUnits.argtypes = ct.c_void_p,
        self.hdll.fmi2_getDisplayUnitByIndex.restype = None
        self.hdll.fmi2_getDisplayUnitByIndex.argtypes = ct.c_void_p, ct.c_int, ct.POINTER(ct.c_char_p), ct.POINTER(ct.c_double),ct.POINTER(ct.c_double),

        self.hdll.fmi2_getReal.restype = ct.c_int
        self.hdll.fmi2_getReal.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_double),
        self.hdll.fmi2_getInteger.restype = ct.c_int
        self.hdll.fmi2_getInteger.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_int),
        self.hdll.fmi2_getBoolean.restype = ct.c_int
        self.hdll.fmi2_getBoolean.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_bool),
        self.hdll.fmi2_getString.restype = ct.c_int
        self.hdll.fmi2_getString.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_char_p),

        self.hdll.fmi2_setReal.restype = ct.c_int
        self.hdll.fmi2_setReal.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_double),
        self.hdll.fmi2_setInteger.restype = ct.c_int
        self.hdll.fmi2_setInteger.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_int),
        self.hdll.fmi2_setBoolean.restype = ct.c_int
        self.hdll.fmi2_setBoolean.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_bool),
        self.hdll.fmi2_setString.restype = ct.c_int
        self.hdll.fmi2_setString.argtypes = ct.c_void_p, ct.POINTER(ct.c_uint), ct.c_size_t,ct.POINTER(ct.c_char_p),

        self.hdll.fmi2_getFMUstate.restype = ct.c_int
        self.hdll.fmi2_getFMUstate.argtypes = ct.c_void_p,ct.c_void_p,
        self.hdll.fmi2_setFMUstate.restype = ct.c_int
        self.hdll.fmi2_setFMUstate.argtypes = ct.c_void_p,ct.c_void_p,
        self.hdll.fmi2_freeFMUstate.restype = ct.c_int
        self.hdll.fmi2_freeFMUstate.argtypes = ct.c_void_p,ct.c_void_p,
        self.hdll.fmi2_serializedFMUstateSize.restype = ct.c_int
        self.hdll.fmi2_serializedFMUstateSize.argtypes = ct.c_void_p,ct.c_void_p,ct.POINTER(ct.c_size_t),
        self.hdll.fmi2_serializeFMUstate.restype = ct.c_int
        self.hdll.fmi2_serializeFMUstate.argtypes = ct.c_void_p,ct.c_void_p,ct.POINTER(ct.c_char),ct.c_size_t,
        self.hdll.fmi2_deSerializeFMUstate.restype = ct.c_int
        self.hdll.fmi2_deSerializeFMUstate.argtypes = ct.c_void_p,ct.POINTER(ct.c_char),ct.c_size_t,ct.c_void_p,

        self.hdll.fmi2_getDirectionalDerivative.restype = ct.c_int
        self.hdll.fmi2_getDirectionalDerivative.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_uint),ct.c_size_t,ct.c_double,ct.c_double,

        self.hdll.fmi2_enterEventMode.restype = ct.c_int
        self.hdll.fmi2_enterEventMode.argtypes = ct.c_void_p,
        self.hdll.fmi2_newDiscreteStates.restype = ct.c_int
        self.hdll.fmi2_newDiscreteStates.argtypes = ct.c_void_p,ct.c_void_p,
        self.hdll.fmi2_enterContinuousTimeMode.restype = ct.c_int
        self.hdll.fmi2_enterContinuousTimeMode.argtypes = ct.c_void_p,
        self.hdll.fmi2_completedIntegratorStep.restype = ct.c_int
        self.hdll.fmi2_completedIntegratorStep.argtypes = ct.c_void_p,ct.c_bool,ct.POINTER(ct.c_bool),ct.POINTER(ct.c_bool),

        self.hdll.fmi2_setTime.restype = ct.c_int
        self.hdll.fmi2_setTime.argtypes = ct.c_void_p,ct.c_double,
        self.hdll.fmi2_setContinuousStates.restype = ct.c_int
        self.hdll.fmi2_setContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,

        self.hdll.fmi2_getDerivatives.restype = ct.c_int
        self.hdll.fmi2_getDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,

        self.hdll.fmi2_getEventIndicators.restype = ct.c_int
        self.hdll.fmi2_getEventIndicators.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,

        self.hdll.fmi2_getContinuousStates.restype = ct.c_int
        self.hdll.fmi2_getContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,

        self.hdll.fmi2_getNominalsOfContinuousStates.restype = ct.c_int
        self.hdll.fmi2_getNominalsOfContinuousStates.argtypes = ct.c_void_p,ct.POINTER(ct.c_double),ct.c_size_t,

        self.hdll.fmi2_setRealInputDerivatives.restype = ct.c_int
        self.hdll.fmi2_setRealInputDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),ct.POINTER(ct.c_double),

        self.hdll.fmi2_getRealOutputDerivatives.restype = ct.c_int
        self.hdll.fmi2_getRealOutputDerivatives.argtypes = ct.c_void_p,ct.POINTER(ct.c_uint),ct.c_size_t,ct.POINTER(ct.c_int),ct.POINTER(ct.c_double),

        self.hdll.fmi2_doStep.restype = ct.c_int
        self.hdll.fmi2_doStep.argtypes = ct.c_void_p,ct.c_double,ct.c_double,ct.c_bool,
        self.hdll.fmi2_cancelStep.restype = ct.c_int
        self.hdll.fmi2_cancelStep.argtypes = ct.c_void_p,

        self.hdll.fmi2_getStatus.restype = ct.c_int
        self.hdll.fmi2_getStatus.argtypes = ct.c_void_p, ct.c_int, ct.POINTER(ct.c_int)
        self.hdll.fmi2_getRealStatus.restype = ct.c_int
        self.hdll.fmi2_getRealStatus.argtypes = ct.c_void_p, ct.c_int, ct.POINTER(ct.c_double),
        self.hdll.fmi2_getIntegerStatus.restype = ct.c_int
        self.hdll.fmi2_getIntegerStatus.argtypes = ct.c_void_p, ct.c_int, ct.POINTER(ct.c_int)
        self.hdll.fmi2_getBooleanStatus.restype = ct.c_int
        self.hdll.fmi2_getBooleanStatus.argtypes = ct.c_void_p, ct.c_int, ct.POINTER(ct.c_bool)
        self.hdll.fmi2_getStringStatus.restype = ct.c_int
        self.hdll.fmi2_getStringStatus.argtypes = ct.c_void_p, ct.c_int,ct.POINTER(ct.c_char_p)

    def translateFmiVersion(self, version):
        match version:
            case 0:
                return "fmiVersionUnknown"
            case 1:
                return "fmiVersion1"
            case 2:
                return "fmiVersion2"
            case 3:
                return "fmiVersion3"

    def translateFmi1Type(self, type):
        match type:
            case 0:
                return "fmi1ModelExchange"
            case 1:
                return "fmi1CoSimulationStandAlone"
            case 2:
                return "fmi1CoSimulationTool"
            case _:
                return ""

    def translateFmi1DataType(self, type):
        match type:
            case 0:
                return "fmi1DataTypeReal"
            case 1:
                return "fmi1DataTypeInteger"
            case 2:
                return "fmi1DataTypeBoolean"
            case 3:
                return "fmi1DataTypeString"
            case 4:
                return "fmi1DataTypeEnumeration"
            case _:
                return ""  

    def translateFmi2DataType(self, type):
        match type:
            case 0:
                return "fmi2DataTypeReal"
            case 1:
                return "fmi2DataTypeInteger"
            case 2:
                return "fmi2DataTypeBoolean"
            case 3:
                return "fmi2DataTypeString"
            case 4:
                return "fmi2DataTypeEnumeration"
            case _:
                return "" 
    
    fmi2CausalityStrings = ["fmi2CausalityInput", "fmi2CausalityOutput", "fmi2CausalityParameter", "fmi2CausalityCalculatedParameter", "fmi2CausalityLocal", "fmi2CausalityIndependent"]
    fmi2VariabilityStrings = ["fmi2VariabilityFixed", "fmi2VariabilityTunable", "fmi2VariabilityConstant", "fmi2VariabilityDiscrete", "fmi2VariabilityContinuous"]
    fmi2InitialStrings = ["fmi2InitialExact", "fmi2InitialApprox", "fmi2InitialCalculated", "fmi2InitialUnknown"]
    
    def fmi4c_getFmiVersion(self):
        return self.translateFmiVersion(self.hdll.fmi4c_getFmiVersion(self.fmu))

    def fmi4c_getErrorMessages(self):
        return self.hdll.fmi4c_getErrorMessages()

    def fmi4c_loadFmu(self, path, instanceName):
        self.fmu = self.hdll.fmi4c_loadFmu(path.encode(), instanceName.encode())
        return self.fmu != 0

    def fmi4c_freeFmu(self):
        self.hdll.fmi4c_freeFmu(self.fmu)

    def fmi1_getType(self):
        return self.translateFmi1Type(self.hdll.fmi1_getType(self.fmu))

    def fmi1_getModelName(self):
        return self.hdll.fmi1_getModelName(self.fmu).decode()

    def fmi1_getModelIdentifier(self):
        return self.hdll.fmi1_getModelIdentifier(self.fmu).decode()

    def fmi1_getGuid(self):
        return self.hdll.fmi1_getGuid(self.fmu).decode()

    def fmi1_getDescription(self):
        ret = self.hdll.fmi1_getDescription(self.fmu)
        if ret is None:
            return ""
        else:
            return ret.decode()


    def fmi1_getAuthor(self):
        ret = self.hdll.fmi1_getAuthor(self.fmu)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getGenerationTool(self):
        ret = self.hdll.fmi1_getGenerationTool(self.fmu)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getGenerationDateAndTime(self):
        ret = self.hdll.fmi1_getGenerationDateAndTime(self.fmu)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getNumberOfContinuousStates(self):
        return self.hdll.fmi1_getNumberOfContinuousStates(self.fmu)

    def fmi1_getNumberOfEventIndicators(self):
        return self.hdll.fmi1_getNumberOfEventIndicators(self.fmu)

    def fmi1_defaultStartTimeDefined(self):
        return self.hdll.fmi1_defaultStartTimeDefined(self.fmu)

    def fmi1_defaultStopTimeDefined(self):
        return self.hdll.fmi1_defaultStopTimeDefined(self.fmu)

    def fmi1_defaultToleranceDefined(self):
        return self.hdll.fmi1_defaultToleranceDefined(self.fmu)

    def fmi1_getDefaultStartTime(self):
        return self.hdll.fmi1_getDefaultStartTime(self.fmu)

    def fmi1_getDefaultStopTime(self):
        return self.hdll.fmi1_getDefaultStopTime(self.fmu)

    def fmi1_getDefaultTolerance(self):
        return self.hdll.fmi1_getDefaultTolerance(self.fmu)

    def fmi1_getNumberOfVariables(self):
        return self.hdll.fmi1_getNumberOfVariables(self.fmu)

    def fmi1_getVariableByIndex(self, i):
        return self.hdll.fmi1_getVariableByIndex(self.fmu, i)

    def fmi1_getVariableByValueReference(self, vr):
        return self.hdll.fmi1_getVariableByValueReference(self.fmu, vr)

    def fmi1_getVariableByName(self, name):
        return self.hdll.fmi1_getVariableByName(self.fmu, name)

    def fmi1_getVariableName(self, var):
        return self.hdll.fmi1_getVariableName(var).decode()

    def fmi1_getVariableDescription(self, var):
        ret = self.hdll.fmi1_getVariableDescription(var)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getVariableQuantity(self, var):
        ret = self.hdll.fmi1_getVariableQuantity(var)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getVariableUnit(self, var):
        ret = self.hdll.fmi1_getVariableUnit(var)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getVariableDisplayUnit(self, var):
        ret = self.hdll.fmi1_getVariableDisplayUnit(var)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi1_getVariableRelativeQuantity(self, var):
        return self.hdll.fmi1_getVariableRelativeQuantity(var)

    def fmi1_getVariableMin(self, var):
        return self.hdll.fmi1_getVariableMin(var)

    def fmi1_getVariableMax(self, var):
        return self.hdll.fmi1_getVariableMax(var)

    def fmi1_getVariableNominal(self, var):
        return self.hdll.fmi1_getVariableNominal(var)

    def fmi1_getNumberOfBaseUnits(self):
        return self.hdll.fmi1_getNumberOfBaseUnits(self.fmu)

    def fmi1_getBaseUnitByIndex(self, id):
        return self.hdll.fmi1_getBaseUnitByIndex(self.fmu, id)

    def fmi1_getBaseUnitUnit(self, unit):
        return self.hdll.fmi1_getBaseUnitUnit(unit).decode()

    def fmi1_getNumberOfDisplayUnits(self, unit):
        return self.hdll.fmi1_getNumberOfDisplayUnits(unit)

    def fmi1_getDisplayUnitUnitByIndex(self, unit, id):
        res = ct.c_char_p()
        dummy1 = ct.c_double()
        dummy2 = ct.c_double()
        self.hdll.fmi1_getDisplayUnitByIndex(unit, id, ct.byref(res), ct.byref(dummy1), ct.byref(dummy2))
        return res.value.decode()

    def fmi1_getVariableHasStartValue(self, var):
        return self.hdll.fmi1_getVariableHasStartValue(var);

    def fmi1_getVariableStartReal(self, var):
        return self.hdll.fmi1_getVariableStartReal(var);

    def fmi1_getVariableStartInteger(self, var):
        return self.hdll.fmi1_getVariableStartInteger(var);

    def fmi1_getVariableStartBoolean(self, var):
        return self.hdll.fmi1_getVariableStartBoolean(var);

    def fmi1_getVariableStartString(self, var):
        return self.hdll.fmi1_getVariableStartString(var);

    def fmi1_getVariableValueReference(self, var):
        return self.hdll.fmi1_getVariableValueReference(var);

    def fmi1_getVariableCausality(self, var):
        return self.hdll.fmi1_getVariableCausality(var);

    def fmi1_getVariableVariability(self, var):
        return self.hdll.fmi1_getVariableVariability(var);

    def fmi1_getAlias(self, var):
        return self.hdll.fmi1_getAlias(var);

    def fmi1_getVariableIsFixed(self, var):
        return self.hdll.fmi1_getVariableIsFixed(var);

    def fmi1_getVariableDataType(self, var):
        return self.translateFmi1DataType(self.hdll.fmi1_getVariableDataType(var));

    def fmi1_getTypesPlatform(self):
        return self.hdll.fmi1_getTypesPlatform(self.fmu).decode();

    def fmi1_getVersion(self):
        return self.hdll.fmi1_getVersion(self.fmu).decode();

    def fmi1_setDebugLogging(self, loggingOn):
        return self.hdll.fmi1_setDebugLogging(self.fmu, loggingOn);

    def fmi1_getReal(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(1,2)
        valuesArray = double_array_type()
        success = self.hdll.fmi1_getReal(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi1_getInteger(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_int * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi1_getInteger(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi1_getBoolean(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_bool * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi1_getBoolean(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi1_getString(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_char_p * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi1_getString(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi1_setReal(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi1_setReal(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi1_setInteger(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_int * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi1_setInteger(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi1_setBoolean(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_bool * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi1_setBoolean(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi1_setString(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_char_p * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi1_setString(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi1_instantiateSlave(self, mimeType, timeOut, visible, interactive, loggingOn):
        return self.hdll.fmi1_instantiateSlave(self.fmu, mimeType, timeOut, visible, interactive, None, None, None, None, loggingOn)

    def fmi1_initializeSlave(self, startTime, stopTimeDefined, stopTime):
        return self.hdll.fmi1_initializeSlave(self.fmu, startTime, stopTimeDefined, stopTime)

    def fmi1_resetSlave(self):
        return self.hdll.fmi1_resetSlave(self.fmu)

    def fmi1_terminateSlave(self):
        return self.hdll.fmi1_terminateSlave(self.fmu)

    def fmi1_freeSlaveInstance(self):
        self.hdll.fmi1_freeSlaveInstance(self.fmu)

    def fmi1_setRealInputDerivatives(self, valueReferences, nValueReferences, orders, values):
        uint_array_type = ct.c_uint * nValueReferences
        int_array_type = ct.c_int * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        ordersArray = int_array_type(*orders)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi1_setRealInputDerivatives(self.fmu, valueReferencesArray, nValueReferences, ordersArray, valuesArray)

    def fmi1_getRealOutputDerivatives(self, valueReferences, nValueReferences, orders):
        uint_array_type = ct.c_uint * nValueReferences
        int_array_type = ct.c_int * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        ordersArray = int_array_type(*orders)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi1_getRealOutputDerivatives(self.fmu, valueReferencesArray, nValueReferences, ordersArray, valuesArray)
        return [success, list(valuesArray)]

    def fmi1_cancelStep(self):
        return self.hdll.fmi1_cancelStep(self.fmu)

    def fmi1_doStep(self, currentCommunicationPoint, communicationStepSize, newStep):
        return self.hdll.fmi1_doStep(self.fmu, currentCommunicationPoint, communicationStepSize, newStep)

    def fmi1_getStatus(self, statusKind):
        value = ct.c_int()
        success = self.hdll.fmi1_getStatus(self.fmu, statusKind, ct.byref(value))
        return [success, value]

    def fmi1_getRealStatus(self, statusKind):
        value = ct.c_double()
        success = self.hdll.fmi1_getRealStatus(self.fmu, statusKind, ct.byref(value))
        return [success, value]

    def fmi1_getIntegerStatus(self, statusKind):
        value = ct.c_int()
        success = self.hdll.fmi1_getIntegerStatus(self.fmu, statusKind, ct.byref(value))
        return [success, value]

    def fmi1_getBooleanStatus(self, statusKind):
        value = ct.c_bool()
        success = self.hdll.fmi1_getBooleanStatus(self.fmu, statusKind, ct.byref(value))
        return [success, value]

    def fmi1_getStringStatus(self, statusKind):
        value = ct.c_char_p()
        success = self.hdll.fmi1_getStringStatus(self.fmu, statusKind, ct.byref(value))
        return [success, value.decode()]

    def fmi1_getModelTypesPlatform(self):
        return self.hdll.fmi1_getModelTypesPlatform(self.fmu).decode()

    def fmi1_instantiateModel(self, loggingOn):
        return self.hdll.fmi1_instantiateModel(self.fmu, None, None, None, loggingOn)

    def fmi1_freeModelInstance(self):
        return self.hdll.fmi1_freeModelInstance(self.fmu)

    def fmi1_setTime(self, time):
        return self.hdll.fmi1_setTime(self.fmu, time)

    def fmi1_setContinuousStates(self, continuousStates, nContinuousStates):
        double_array_type = ct.c_double * nContinuousStates
        continuousStatesArray = double_array_type(*continuousStates)
        return self.hdll.fmi1_setContinuousStates(self.fmu, continuousStatesArray, nContinuousStates)

    def fmi1_completedIntegratorStep(self, callEventUpdate):
        return self.hdll.fmi1_completedIntegratorStep(self.fmu, callEventUpdate)

    def fmi1_initialize(self, toleranceControlled, relativeTolerance, eventInfo):
        return self.hdll.fmi1_initialize(self.fmu, toleranceControlled, relativeTolerance, eventInfo)

    def fmi1_getDerivatives(self, derivatives, nDerivatives):
        double_array_type = ct.c_double * nDerivatives
        derivativesArray = double_array_type(*derivatives)
        success = self.hdll.fmi1_getDerivatives(self.fmu, derivativesArray, nDerivatives)
        return [success, list(derivativesArray)]

    def fmi1_getEventIndicators(self, indicators, nIndicators):
        double_array_type = ct.c_double * nIndicators
        indicatorsArray = double_array_type(*indicators)
        success = self.hdll.fmi1_getEventIndicators(self.fmu, indicatorsArray, nIndicators)
        return [success, list(indicatorsArray)]

    def fmi1_eventUpdate(self, intermediateResults, eventInfo):
        return self.hdll.fmi1_eventUpdate(self.fmu, intermediateResults, eventInfo)

    def fmi1_getContinuousStates(self, states, nStates):
        double_array_type = ct.c_double * nStates
        statesArray = double_array_type(*states)
        success = self.hdll.fmi1_getContinuousStates(self.fmu, statesArray, nStates)
        return [success, list(statesArray)]

    def fmi1_getNominalContinuousStates(self, nominals, nNominals):
        double_array_type = ct.c_double * nNominals
        nominalsArray = double_array_type(*nominals)
        success = self.hdll.fmi1_getNominalContinuousStates(self.fmu, nominalsArray, nNominals)
        return [success, list(nominalsArray)]


    def fmi1_getStateValueReferences(self, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        valueReferencesArray = uint_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi1_getStateValueReferences(self.fmu, valueReferencesArray, nValueReferences)
        return [success, list(valueReferencesArray)]

    def fmi1_terminate(self):
        return self.hdll.fmi1_terminate(self.fmu)

    def fmi2_defaultStartTimeDefined(self):
        return self.hdll.fmi2_defaultStartTimeDefined(self.fmu)

    def fmi2_defaultStopTimeDefined(self):
        return self.hdll.fmi2_defaultStopTimeDefined(self.fmu)

    def fmi2_defaultToleranceDefined(self):
        return self.hdll.fmi2_defaultToleranceDefined(self.fmu)

    def fmi2_defaultStepSizeDefined(self):
        return self.hdll.fmi2_defaultStepSizeDefined(self.fmu)

    def fmi2_getDefaultStartTime(self):
        return self.hdll.fmi2_getDefaultStartTime(self.fmu)

    def fmi2_getDefaultStopTime(self):
        return self.hdll.fmi2_getDefaultStopTime(self.fmu)

    def fmi2_getDefaultTolerance(self):
        return self.hdll.fmi2_getDefaultTolerance(self.fmu)

    def fmi2_getDefaultStepSize(self):
        return self.hdll.fmi2_getDefaultStepSize(self.fmu)

    def fmi2_getNumberOfVariables(self):
        return self.hdll.fmi2_getNumberOfVariables(self.fmu)

    def fmi2_getVariableByIndex(self, i):
        return self.hdll.fmi2_getVariableByIndex(self.fmu, i)

    def fmi2_getVariableByValueReference(self, vr):
        return self.hdll.fmi2_getVariableByValueReference(self.fmu, vr)

    def fmi2_getVariableByName(self, name):
        return self.hdll.fmi2_getVariableByName(self.fmu, name)

    def fmi2_getVariableName(self, var):
        return self.hdll.fmi2_getVariableName(var).decode()

    def fmi2_getVariableDescription(self, var):
        ret = self.hdll.fmi2_getVariableDescription(var)
        if ret is None:
            return ""
        else:
            return ret.decode()

    def fmi2_getFmiVersion(self):
        return self.hdll.fmi2_getFmiVersion(self.fmu).decode()

    def fmi2_getAuthor(self):
        return self.hdll.fmi2_getAuthor(self.fmu).decode()

    def fmi2_getModelName(self):
        return self.hdll.fmi2_getModelName(self.fmu).decode()

    def fmi2_getModelDescription(self):
        return self.hdll.fmi2_getModelDescription(self.fmu).decode()

    def fmi2_getCopyright(self):
        return self.hdll.fmi2_getCopyright(self.fmu).decode()

    def fmi2_getLicense(self):
        return self.hdll.fmi2_getLicense(self.fmu).decode()

    def fmi2_getGenerationTool(self):
        return self.hdll.fmi2_getGenerationTool(self.fmu).decode()

    def fmi2_getGenerationDateAndTime(self):
        return self.hdll.fmi2_getGenerationDateAndTime(self.fmu).decode()

    def fmi2_getVariableNamingConvention(self):
        return self.hdll.fmi2_getVariableNamingConvention(self.fmu).decode()

    def fmi2_getVariableDerivativeIndex(self, var):
        return self.hdll.fmi2_getVariableDerivativeIndex(var)

    def fmi2_getVariableQuantity(self, var):
        ret = self.hdll.fmi2_getVariableQuantity(var)
        if ret is None:
            return ""
        else:
            return ret.decode()        

    def fmi2_getVariableUnit(self, var):
        ret = self.hdll.fmi2_getVariableUnit(var)
        if ret is None:
            return ""
        else:
            return ret.decode()        

    def fmi2_getVariableDisplayUnit(self, var):
        ret = self.hdll.fmi2_getVariableDisplayUnit(var)
        if ret is None:
            return ""
        else:
            return ret.decode()        

    def fmi2_getVariableRelativeQuantity(self, var):
        ret = self.hdll.fmi2_getVariableRelativeQuantity(var)
        if ret is None:
            return ""
        else:
            return ret.decode()        

    def fmi2_getVariableRelativeQuantity(self, var):
        return self.hdll.fmi2_getVariableRelativeQuantity(var)

    def fmi2_getVariableMin(self, var):
        return self.hdll.fmi2_getVariableMin(var)

    def fmi2_getVariableMax(self, var):
        return self.hdll.fmi2_getVariableMax(var)

    def fmi2_getVariableNominal(self, var):
        return self.hdll.fmi2_getVariableNominal(var)

    def fmi2_getVariableUnbounded(self, var):
        return self.hdll.fmi2_getVariableUnbounded(var)        
        
    def fmi2_getVariableHasStartValue(self, var):
        return self.hdll.fmi2_getVariableHasStartValue(var)

    def fmi2_getVariableStartReal(self, var):
        return self.hdll.fmi2_getVariableStartReal(var)

    def fmi2_getVariableStartInteger(self, var):
        return self.hdll.fmi2_getVariableStartInteger(var)

    def fmi2_getVariableStartBoolean(self, var):
        return self.hdll.fmi2_getVariableStartBoolean(var)

    def fmi2_getVariableStartString(self, var):
        return self.hdll.fmi2_getVariableStartString(var)

    def fmi2_getVariableValueReference(self, var):
        return self.hdll.fmi2_getVariableValueReference(var)

    def fmi2_getVariableCausality(self, var):
        return self.fmi2CausalityStrings[self.hdll.fmi2_getVariableCausality(var)]

    def fmi2_getVariableVariability(self, var):
        return self.fmi2VariabilityStrings[self.hdll.fmi2_getVariableVariability(var)]

    def fmi2_getVariableInitial(self, var):
        return self.fmi2InitialStrings[self.hdll.fmi2_getVariableInitial(var)]

    def fmi2_getVariableCanHandleMultipleSetPerTimeInstant(self, var):
        return self.hdll.fmi2_getVariableCanHandleMultipleSetPerTimeInstant(var)

    def fmi2_getVariableDataType(self, var):
        return self.translateFmi2DataType(self.hdll.fmi2_getVariableDataType(var))

    def fmi2_getTypesPlatform(self):
        return self.hdll.fmi2_getTypesPlatform(self.fmu).decode()

    def fmi2_getVersion(self):
        return self.hdll.fmi2_getVersion(self.fmu).decode()

    def fmi2_setDebugLogging(self, loggingOn, nCategories, categories):
        return self.hdll.fmi2_setDebugLogging(self.fmu, loggingOn, nCategories, categories)

    def fmi2_getGuid(self):
        return self.hdll.fmi2_getGuid(self.fmu).decode()

    def fmi2cs_getModelIdentifier(self):
        return self.hdll.fmi2cs_getModelIdentifier(self.fmu).decode()
        
    def fmi2cs_getCanHandleVariableCommunicationStepSize(self):
        return self.hdll.fmi2cs_getCanHandleVariableCommunicationStepSize(self.fmu)

    def fmi2cs_getCanInterpolateInputs(self):
        return self.hdll.fmi2cs_getCanInterpolateInputs(self.fmu)

    def fmi2cs_getMaxOutputDerivativeOrder(self):
        return self.hdll.fmi2cs_getMaxOutputDerivativeOrder(self.fmu)

    def fmi2cs_getCanRunAsynchronuously(self):
        return self.hdll.fmi2cs_getCanRunAsynchronuously(self.fmu)

    def fmi2cs_getNeedsExecutionTool(self):
        return self.hdll.fmi2cs_getNeedsExecutionTool(self.fmu)

    def fmi2cs_getCanBeInstantiatedOnlyOncePerProcess(self):
        return self.hdll.fmi2cs_getCanBeInstantiatedOnlyOncePerProcess(self.fmu)

    def fmi2cs_getCanNotUseMemoryManagementFunctions(self):
        return self.hdll.fmi2cs_getCanNotUseMemoryManagementFunctions(self.fmu)

    def fmi2cs_getCanGetAndSetFMUState(self):
        return self.hdll.fmi2cs_getCanGetAndSetFMUState(self.fmu)

    def fmi2cs_getCanSerializeFMUState(self):
        return self.hdll.fmi2cs_getCanSerializeFMUState(self.fmu)

    def fmi2cs_getProvidesDirectionalDerivative(self):
        return self.hdll.fmi2cs_getProvidesDirectionalDerivative(self.fmu)

    def fmi2me_getModelIdentifier(self):
        return self.hdll.fmi2me_getModelIdentifier(self.fmu).decode()

    def fmi2me_getCompletedIntegratorStepNotNeeded(self):
        return self.hdll.fmi2me_getCompletedIntegratorStepNotNeeded(self.fmu)

    def fmi2me_getNeedsExecutionTool(self):
        return self.hdll.fmi2me_getNeedsExecutionTool(self.fmu)

    def fmi2me_getCanBeInstantiatedOnlyOncePerProcess(self):
        return self.hdll.fmi2me_getCanBeInstantiatedOnlyOncePerProcess(self.fmu)

    def fmi2me_getCanNotUseMemoryManagementFunctions(self):
        return self.hdll.fmi2me_getCanNotUseMemoryManagementFunctions(self.fmu)

    def fmi2me_getCanGetAndSetFMUState(self):
        return self.hdll.fmi2me_getCanGetAndSetFMUState(self.fmu)

    def fmi2me_getCanSerializeFMUState(self):
        return self.hdll.fmi2me_getCanSerializeFMUState(self.fmu)

    def fmi2me_getProvidesDirectionalDerivative(self):
        return self.hdll.fmi2me_getProvidesDirectionalDerivative(self.fmu)

    def fmi2_getNumberOfContinuousStates(self):
        return self.hdll.fmi2_getNumberOfContinuousStates(self.fmu)

    def fmi2_getNumberOfEventIndicators(self):
        return self.hdll.fmi2_getNumberOfEventIndicators(self.fmu)

    def fmi2_getSupportsCoSimulation(self):
        return self.hdll.fmi2_getSupportsCoSimulation(self.fmu)

    def fmi2_getSupportsModelExchange(self):
        return self.hdll.fmi2_getSupportsModelExchange(self.fmu)

    def fmi2_instantiate(self, type, visible,  loggingOn):
        return self.hdll.fmi2_instantiate(self.fmu,  type, None, None, None, None, None,  visible,  loggingOn)

    def fmi2_freeInstance(self):
        return self.hdll.fmi2_freeInstance(self.fmu)

    def fmi2_setupExperiment(self, toleranceDefined, tolerance, startTime, stopTimeDefined, stopTime):
        return self.hdll.fmi2_setupExperiment(self.fmu, toleranceDefined, tolerance, startTime, stopTimeDefined, stopTime)

    def fmi2_enterInitializationMode(self):
        return self.hdll.fmi2_enterInitializationMode(self.fmu)

    def fmi2_exitInitializationMode(self):
        return self.hdll.fmi2_exitInitializationMode(self.fmu)

    def fmi2_terminate(self):
        return self.hdll.fmi2_terminate(self.fmu)

    def fmi2_reset(self):
        return self.hdll.fmi2_reset(self.fmu)

    def fmi2_getNumberOfUnits(self):
        return self.hdll.fmi2_getNumberOfUnits(self.fmu)

    def fmi2_getUnitByIndex(self, i):
        return self.hdll.fmi2_getUnitByIndex(self.fmu, i)

    def fmi2_getUnitName(self, unit):
        return self.hdll.fmi2_getUnitName(unit)

    def fmi2_hasBaseUnit(self, unit):
        return self.hdll.fmi2_hasBaseUnit(unit)

    def fmi2_getBaseUnit(self, unit):
        factor = ct.c_double()
        offset = ct.c_double()
        kg = ct.c_int()
        m = ct.c_int()
        s = ct.c_int()
        A = ct.c_int()
        K = ct.c_int()
        mol = ct.c_int()
        cd = ct.c_int()
        rad = ct.c_int()
        self.hdll.fmi2_getBaseUnit(unit, ct.byref(factor), ct.byref(offset), ct.byref(kg), ct.byref(m), ct.byref(s), ct.byref(A), ct.byref(K), ct.byref(mol), ct.byref(cd), ct.byref(rad))
        return (factor.value, offset.value, kg.value, m.value, s.value, A.value, K.value, mol.value, cd.value, rad.value)

    def fmi2_getNumberOfDisplayUnits(self, unit):
        return self.hdll.fmi2_getNumberOfDisplayUnits(unit)

    def fmi2_getDisplayUnitByIndex(self, unit, id):
        name = ct.c_char_p()
        factor = ct.c_double()
        offset = ct.c_double()
        self.hdll.fmi2_getDisplayUnitByIndex(unit, id, ct.byref(name), ct.byref(factor), ct.byref(offset))
        return (name.value.decode(), factor.value, offset.value)

    def fmi2_getReal(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(1,2)
        valuesArray = double_array_type()
        success = self.hdll.fmi2_getReal(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi2_getInteger(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_int * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi2_getInteger(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi2_getBoolean(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_bool * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi2_getBoolean(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi2_getString(self, valueReferences, nValueReferences):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_char_p * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*[1]*nValueReferences)
        success = self.hdll.fmi2_getString(self.fmu, valueReferencesArray, nValueReferences, valuesArray)
        return [success, list(valuesArray)]

    def fmi2_setReal(self, valueReferences,  nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_double * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi2_setReal(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi2_setInteger(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_int * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi2_setInteger(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi2_setBoolean(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_bool * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi2_setBoolean(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi2_setString(self, valueReferences, nValueReferences, values):
        uint_array_type = ct.c_uint * nValueReferences
        double_array_type = ct.c_char_p * nValueReferences
        valueReferencesArray = uint_array_type(*valueReferences)
        valuesArray = double_array_type(*values)
        return self.hdll.fmi2_setString(self.fmu, valueReferencesArray, nValueReferences, valuesArray)

    def fmi2_getFMUstate(self, FMUstate):
        return self.hdll.fmi2_getFMUstate(self.fmu, FMUstate)

    def fmi2_setFMUstate(self, FMUstate):
        return self.hdll.fmi2_setFMUstate(self.fmu, FMUstate)

    def fmi2_freeFMUstate(self, FMUstate):
        return self.hdll.fmi2_freeFMUstate(self.fmu, FMUstate)

    def fmi2_serializedFMUstateSize(self, FMUstate,  size):
        return self.hdll.fmi2_serializedFMUstateSize(self.fmu, FMUstate,  size)

    def fmi2_serializeFMUstate(self, FMUstate, serializedState,  size):
        return self.hdll.fmi2_serializeFMUstate(self.fmu, FMUstate, serializedState,  size)

    def fmi2_deSerializeFMUstate(self, serializedState,  size, FMUstate):
        return self.hdll.fmi2_deSerializeFMUstate(self.fmu, serializedState,  size, FMUstate)

    def fmi2_getDirectionalDerivative(self, unknownReferences,  nUnknown, knownReferences,  nKnown, dvKnown, dvUnknown):
        return self.hdll.fmi2_getDirectionalDerivative(self.fmu, unknownReferences,  nUnknown, knownReferences,  nKnown, dvKnown, dvUnknown)

    def fmi2_enterEventMode(self):
        return self.hdll.fmi2_enterEventMode(self.fmu)

    def fmi2_newDiscreteStates(self, eventInfo):
        return self.hdll.fmi2_newDiscreteStates(self.fmu, eventInfo)

    def fmi2_enterContinuousTimeMode(self):
        return self.hdll.fmi2_enterContinuousTimeMode(self.fmu)

    def fmi2_completedIntegratorStep(self,  noSetFMUStatePriorToCurrentPoint,  enterEventMode,  terminateSimulation):
        return self.hdll.fmi2_completedIntegratorStep(self.fmu,  noSetFMUStatePriorToCurrentPoint,  enterEventMode,  terminateSimulation)

    def fmi2_setTime(self, time):
        return self.hdll.fmi2_setTime(self.fmu, time)

    def fmi2_setContinuousStates(self, x,  nx):
        return self.hdll.fmi2_setContinuousStates(self.fmu, x,  nx)

    def fmi2_getDerivatives(self, derivatives,  nx):
        return self.hdll.fmi2_getDerivatives(self.fmu, derivatives,  nx)

    def fmi2_getEventIndicators(self, eventIndicators,  ni):
        return self.hdll.fmi2_getEventIndicators(self.fmu, eventIndicators,  ni)

    def fmi2_getContinuousStates(self, x,  nx):
        return self.hdll.fmi2_getContinuousStates(self.fmu, x,  nx)

    def fmi2_getNominalsOfContinuousStates(self, x_nominal,  nx):
        return self.hdll.fmi2_getNominalsOfContinuousStates(self.fmu, x_nominal,  nx)


    def fmi2_setRealInputDerivatives(self, vr,  nvr,  order, value):
        return self.hdll.fmi2_setRealInputDerivatives(self.fmu, vr,  nvr,  order, value)

    def fmi2_getRealOutputDerivatives(self, vr,  nvr,  order, value):
        return self.hdll.fmi2_getRealOutputDerivatives(self.fmu, vr,  nvr,  order, value)

    def fmi2_doStep(self, currentCommunicationPoint, communicationStepSize, noSetFMUStatePriorToCurrentPoint):
        return self.hdll.fmi2_doStep(self.fmu, currentCommunicationPoint, communicationStepSize, noSetFMUStatePriorToCurrentPoint)

    def fmi2_cancelStep(self):
        return self.hdll.fmi2_cancelStep(self.fmu)

    def fmi2_getStatus(self, s, value):
        return self.hdll.fmi2_getStatus(self.fmu, s, value)

    def fmi2_getRealStatus(self, s, value):
        return self.hdll.fmi2_getRealStatus(self.fmu, s, value)

    def fmi2_getIntegerStatus(self, s, value):
        return self.hdll.fmi2_getIntegerStatus(self.fmu, s, value)

    def fmi2_getBooleanStatus(self, s,  value):
        return self.hdll.fmi2_getBooleanStatus(self.fmu, s,  value)

    def fmi2_getStringStatus(self, s, value):
        return self.hdll.fmi2_getStringStatus(self.fmu, s, value)
