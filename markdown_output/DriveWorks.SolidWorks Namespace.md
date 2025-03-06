![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.SolidWorks Namespace   
See Also [Inheritance Hierarchy](topic13346.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13345.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) : DriveWorks.SolidWorks Namespace  
---  
  
Glossary Item Box

Provides common SolidWorks services and types. 

# ![](dotnetimages/collapse.gif)Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [CaptureViewAttribute](topic13455.md) | An attribute used to flag types in assemblies as being Capture Views.  
![Class](dotnetimages/Class.gif)| [CaptureViewHostStates](topic13474.md) | Provides a list of common [ICaptureViewHost](topic13363.md) states.  
![Class](dotnetimages/Class.gif)| [ClipboardSupport](topic13507.md) | Provides commonly used functionality when dealing with the clipboard.  
![Class](dotnetimages/Class.gif)| [ComponentRegisteredWithDifferentPathException](topic13517.md) | Throw when an attempt is made to captured a component that is already captured with a different path.  
![Class](dotnetimages/Class.gif)| [CustomPropertyValueCondition](topic13527.md) |   
![Class](dotnetimages/Class.gif)| [DimensionValueCondition](topic13536.md) |   
![Class](dotnetimages/Class.gif)| [DriveWorksCaptureViewNames](topic13545.md) | Represents a list of the names of the DriveWorks standard [ICaptureView](topic13347.md)s.  
![Class](dotnetimages/Class.gif)| [FileExtensionAttribute](topic13564.md) | Represents an attribute that is specific to a file extension.  
![Class](dotnetimages/Class.gif)| [FileFormatGenerateTaskAttribute](topic13571.md) | Attribute that should be assigned to tasks that inherits from the file format generator base task.  
![Class](dotnetimages/Class.gif)| [FileFormatGenerator](topic13579.md) | Provides a base for SolidWorks file format generators.  
![Class](dotnetimages/Class.gif)| [FileFormatGeneratorAttribute](topic13607.md) | Attribute that should be assigned to inheritors of [FileFormatGenerator](topic13579.md) to specify their target file extensions.  
![Class](dotnetimages/Class.gif)| [FileFormatParameterInfo](topic13615.md) | Provides information about a file format.  
![Class](dotnetimages/Class.gif)| [FileFormatStandardParameters](topic13624.md) | Provides parameter names of all standard additional file format types.  
![Class](dotnetimages/Class.gif)| [FileOpenNotifyEventArgs](topic13653.md) | Provides event data for the FileOpenPreNotify SolidWorks event that gets raised when an existing file has been opened.  
![Class](dotnetimages/Class.gif)| [FileSavePostNotifyEventArgs](topic13661.md) | Provides event data for the FileSavePostNotify SolidWorks event that gets raised when a file is saved.  
![Class](dotnetimages/Class.gif)| [FormatGeneratorFactory](topic13670.md) | Provides a creator for file format generators.  
![Class](dotnetimages/Class.gif)| [GenerationTask](topic13678.md) | Provides the base class for all generation tasks.  
![Class](dotnetimages/Class.gif)| [GenerationTaskAttribute](topic13693.md) | Attribute to be assigned to inheritors of the [GenerationTask](topic13678.md) class to provide additional information about the task.  
![Class](dotnetimages/Class.gif)| [GenerationTaskCondition](topic13707.md) | Represents a condition which governs whether a [GenerationTask](topic13678.md) will run during generation.  
![Class](dotnetimages/Class.gif)| [GenerationTaskConditionAttribute](topic13721.md) | Attribute to be assigned to inheritors of the [GenerationTaskCondition](topic13707.md) class to provide additional information about the condition.  
![Class](dotnetimages/Class.gif)| [GenerationTaskScopeProvider](topic13735.md) |   
![Class](dotnetimages/Class.gif)| [GenerationTaskTypeKeys](topic13743.md) | Gets the constants that identifies the component type specific [DriveWorks.Components.Tasks.ComponentTask](topic6407.md)s in the DriveWorks Engine.  
![Class](dotnetimages/Class.gif)| [GroupContainsDuplicateComponentDataException](topic13754.md) | Represents an exception thrown when the group data contains duplicate captured components.  
![Class](dotnetimages/Class.gif)| [GroupDataChangedByExternalProgramException](topic13763.md) | Represents an exception thrown when the group data has been changed by another program.  
![Class](dotnetimages/Class.gif)| [HasCustomPropertyCondition](topic13772.md) | Represents a condition for a [GenerationTask](topic13678.md) that checks to see whether a Custom Property exists in the SOLIDWOKRS model.  
![Class](dotnetimages/Class.gif)| [MassPropertyCondition](topic13781.md) |   
![Class](dotnetimages/Class.gif)| [MergedAnnotationInfo](topic13790.md) | Represents merge information for annotations.  
![Class](dotnetimages/Class.gif)| [MergedBreakLineInfo](topic13797.md) | Represents merge information for breaklines.  
![Class](dotnetimages/Class.gif)| [MergedDrawingInfo](topic13815.md) | Represents merge information for drawings.  
![Class](dotnetimages/Class.gif)| [MergedItem<TDriveWorks,TSolidWorks>](topic13826.md) | Provides a base class for merged items.  
![Class](dotnetimages/Class.gif)| [MergedLayerInfo](topic13835.md) | Represents merge information for layers.  
![Class](dotnetimages/Class.gif)| [MergedSheetInfo](topic13842.md) | Represents merge information for sheets.  
![Class](dotnetimages/Class.gif)| [MergedViewDimensionInfo](topic13851.md) | Represents merge information for view dimensions.  
![Class](dotnetimages/Class.gif)| [MergedViewInfo](topic13858.md) | Represents merge information for views.  
![Class](dotnetimages/Class.gif)| [NewSelectionNotifyEventArgs](topic13867.md) | Provides event data for the [NewSelectionNotifyEventArgs](topic13867.md) SolidWorks event that gets raised when the selection list has changed.  
![Class](dotnetimages/Class.gif)| [ProhibitedStatesAttribute](topic13875.md) | An attribute used to flag all prohibited the application states where this entity should not be visible if the application is in any of them.  
![Class](dotnetimages/Class.gif)| [RebuildResult](topic13883.md) | Represents the result of attempting to rebuild the model until it stabilizes.  
![Class](dotnetimages/Class.gif)| [ReportProcessStatusViewModel](topic13891.md) |   
![Class](dotnetimages/Class.gif)| [RequiredStatesAttribute](topic13901.md) | An attribute used to flag all the states the application is required to be in for this entity to be visible.  
![Class](dotnetimages/Class.gif)| [ResultEventArgs](topic13909.md) | Represents a wrapper event args for events that expects event handlers to return a value.  
![Class](dotnetimages/Class.gif)| [VerifyingGenerationRequiredEventArgs](topic13917.md) | Represents the event data for the VerifyingGenerationRequired event.  
  
# ![](dotnetimages/collapse.gif)Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [ICaptureView](topic13347.md) | Represents a view within the DriveWorks Capture Assistant.  
![Interface](dotnetimages/Interface.gif)| [ICaptureViewEnvironment](topic13353.md) | Represents the interaction between [ICaptureView](topic13347.md)s and their host.  
![Interface](dotnetimages/Interface.gif)| [ICaptureViewHost](topic13363.md) | Represents DriveWorks inside the SolidWorks task pane.  
![Interface](dotnetimages/Interface.gif)| [IComponentManager](topic13385.md) | Represents the component manager that manages a cached version of all captured components in the current group.  
![Interface](dotnetimages/Interface.gif)| [ISolidWorksService](topic13411.md) | Provides access to SolidWorks from a DriveWorks application.  
![Interface](dotnetimages/Interface.gif)| [ISolidWorksState](topic13419.md) | Represents the current SolidWorks state.  
![Interface](dotnetimages/Interface.gif)| [ISpecificationsManager](topic13440.md) | Represents common specification manager functionality.  
  
# ![](dotnetimages/collapse.gif)Delegates

| Delegate| Description  
---|---|---  
![Delegate](dotnetimages/Delegate.gif)| [FileFormatGenerator.AdditionalFileGeneratedEventHandler](topic13924.md) |   
  
# ![](dotnetimages/collapse.gif)Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [FeatureClass](topic13450.md) | Represents the different classes of feature as recognized by DriveWorks.  
![Enumeration](dotnetimages/Enumeration.gif)| [FullFilePathBuildStatus](topic13451.md) | Represents the different states of building a full file path.  
![Enumeration](dotnetimages/Enumeration.gif)| [GenerationTaskScope](topic13452.md) | Specifies the type of SOLIDWORKS components a [GenerationTask](topic13678.md) support.  
![Enumeration](dotnetimages/Enumeration.gif)| [MergedItemState](topic13453.md) | Represents the state of a merged item.  
![Enumeration](dotnetimages/Enumeration.gif)| [TaskExecutionResult](topic13454.md) | Represents the execution result of a [GenerationTask](topic13678.md).  
  
# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.SolidWorks Assembly](topic13342.md)


