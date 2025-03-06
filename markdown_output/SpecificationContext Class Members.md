![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationContext Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11149.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationContext Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [SpecificationContext](topic11149.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [ActiveDialog](topic11195.md)| Gets the latest dialog if the specification is running and one or more dialogs are active.   
![Public Property](dotnetimages/publicProperty.gif)| [ActiveDialogOrForm](topic11196.md)| Gets the active dialog if one is shown, otherwise, gets the active form.   
![Public Property](dotnetimages/publicProperty.gif)| [ActiveForm](topic11197.md)| Gets the active form in the specification navigation if the specification is running.   
![Public Property](dotnetimages/publicProperty.gif)| [AdditionalFoldersRelativeToSpecificationFolder](topic11198.md)| Gets whether additional folders' paths are calculated relative to the specification's folder, if false, they are calculated relative to the default specification folder instead.   
![Public Property](dotnetimages/publicProperty.gif)| [CurrentState](topic11199.md)| Gets the current specification-flow state of the open specification.   
![Public Property](dotnetimages/publicProperty.gif)| [DesignMasterPath](topic11200.md)| Gets the fully-qualified path to the specification's cached version of the project's design master (see remarks for details).   
![Public Property](dotnetimages/publicProperty.gif)| [DocumentsRelativeToSpecificationFolder](topic11201.md)| Gets whether documents' paths are calculated relative to the specification's folder, if false, they are calculated relative to the default specification folder instead.   
![Public Property](dotnetimages/publicProperty.gif)| [Environment](topic11202.md)| Gets the settings for the specification environment.   
![Public Property](dotnetimages/publicProperty.gif)| [Group](topic11203.md)| Gets the group containing the project to be specified.   
![Public Property](dotnetimages/publicProperty.gif)| [HideMetadataDirectory](topic11204.md)| Gets whether the metadata directory is hidden if used.   
![Public Property](dotnetimages/publicProperty.gif)| [HostingControl](topic11205.md)| The parent specification host control for the specification, if there is one.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic11206.md)| Gets the identifier which uniquely identifies the current specification.   
![Public Property](dotnetimages/publicProperty.gif)| [InCancel](topic11207.md)| Determines whether the specification context is in the process of cancelling.   
![Public Property](dotnetimages/publicProperty.gif)| [InOperation](topic11208.md)| Determines whether the specification context is in the process of invoking an operation.   
![Public Property](dotnetimages/publicProperty.gif)| [InTransition](topic11209.md)| Determines whether the specification context is in the process of invoking a transition.   
![Public Property](dotnetimages/publicProperty.gif)| [IsArchived](topic11210.md)| Determines whether the specification is marked as archived from view.   
![Public Property](dotnetimages/publicProperty.gif)| [IsEmbedded](topic11211.md)| Returns whether or not this is an embedded specification.   
![Public Property](dotnetimages/publicProperty.gif)| [IsInRunningState](topic11212.md)| Determines whether the specification is in a running state, as opposed to paused or automatic.   
![Public Property](dotnetimages/publicProperty.gif)| [IsLoaded](topic11213.md)| Determines whether the specification is loaded.   
![Public Property](dotnetimages/publicProperty.gif)| [IsRuleProfilingEnabled](topic11214.md)| Gets/sets whether projects loaded in this specification group should have profiling enabled.   
![Public Property](dotnetimages/publicProperty.gif)| [IsRunning](topic11215.md)| Determines whether the specification is running. See remarks for details.   
![Public Property](dotnetimages/publicProperty.gif)| [MetadataDirectoryName](topic11216.md)| Gets the name of a directory which will act as a container for artifacts used to manage a specification, or a null reference to put them in the specification folder.   
![Public Property](dotnetimages/publicProperty.gif)| [OriginalSpecificationName](topic11217.md)| If the specification is in a transition, gets the name of the specification passed to the [Open](topic11190.md) method when the specification was originally opened.   
![Public Property](dotnetimages/publicProperty.gif)| [ParentContext](topic11218.md)| Gets the context of the parent specification if the current specification is a child specification.   
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic11219.md)| Gets the project being specified.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectDirectory](topic11220.md)| Gets the fully-qualified path to the directory containing the project on which the specification is based.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectFilePath](topic11221.md)| Gets the fully-qualified path to the specification's cached version of the project file (see remarks for details).   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectId](topic11222.md)| Gets the id of the project for this specification context.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectName](topic11223.md)| Gets the name of the project for this specification context.   
![Public Property](dotnetimages/publicProperty.gif)| [Report](topic11224.md)| Gets the active report object.   
![Public Property](dotnetimages/publicProperty.gif)| [RootContext](topic11225.md)| Gets the root [SpecificationContext](topic11149.md).   
![Public Property](dotnetimages/publicProperty.gif)| [RootTemporaryFilesDirectory](topic11226.md)| Gets information about the directory which is the root of all temporary folders created for specifications related to this context.   
![Public Property](dotnetimages/publicProperty.gif)| [ShowRunningUserInterface](topic11227.md)| Gets/sets whether this specification should have its form UI shown when it starts running.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationDirectory](topic11228.md)| Gets the fully-qualified path to the specification directory.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationFilePath](topic11229.md)| Gets the fully-qualified path to the specification file.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationName](topic11230.md)| Gets the specification name of a loaded or running specification.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationTags](topic11231.md)| Gets the tags associated with this specification.   
![Public Property](dotnetimages/publicProperty.gif)| [TaskList](topic11232.md)| Gets the task list for the specification.   
![Public Property](dotnetimages/publicProperty.gif)| [TemporaryDesignMasterPath](topic11233.md)| Gets the fully-qualified path to the context's temporary copy of the design-master.   
![Public Property](dotnetimages/publicProperty.gif)| [TemporaryFilesDirectory](topic11234.md)| Gets the fully-qualified path to the context's temporary files directory.   
![Public Property](dotnetimages/publicProperty.gif)| [TemporaryProjectFilePath](topic11235.md)| Gets the fully-qualified path to the context's temporary copy of the project file.   
![Public Property](dotnetimages/publicProperty.gif)| [Type](topic11236.md)| Gets the type of the specification.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [Cancel](topic11160.md)| Cancels the specification.   
![Public Method](dotnetimages/publicMethod.gif)| [Copy](topic11161.md)| Overloaded. Starts a new specification based on the given specification.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic11164.md)| Deletes the specification represented by the context.   
![Public Method](dotnetimages/publicMethod.gif)| [DriveInputs](topic11165.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [EnsureRunnableProject](topic11166.md)| Returns if the current specification is valid or not.   
![Public Method](dotnetimages/publicMethod.gif)| [GetExpectedSpecificationDirectory](topic11167.md)| Gets the current expected specification directory of a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetOperations](topic11168.md)| Gets an array of transitions with the evaluated result of their conditions.   
![Public Method](dotnetimages/publicMethod.gif)| [GetTransitions](topic11169.md)| Gets an array of transitions with the evaluated result of their conditions.   
![Public Method](dotnetimages/publicMethod.gif)| [InvokeOperation](topic11170.md)| Overloaded. Invokes the specified operation.   
![Public Method](dotnetimages/publicMethod.gif)| [InvokeTransition](topic11173.md)| Overloaded. Invokes the specified transition.   
![Public Method](dotnetimages/publicMethod.gif)| [Navigate](topic11176.md)| Navigates the forms in a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| [NavigateTo](topic11177.md)| Navigates to a specified form in a running specification.   
![Public Method](dotnetimages/publicMethod.gif)| [OnForceFormUpdateAsync](topic11188.md)| Raises the [ForceFormUpdate](topic11258.md) event, as well as despatching an asynchronus update event on the root [SpecificationContext](topic11149.md).   
![Public Method](dotnetimages/publicMethod.gif)| [OnFormValueChanged](topic11189.md)| Raises the [FormValueChanged](topic11259.md) event. The event data for the event.   
![Public Method](dotnetimages/publicMethod.gif)| [Open](topic11190.md)| Opens the given existing specification.   
![Public Method](dotnetimages/publicMethod.gif)| [QueryOperation](topic11191.md)| Queries an operation's tasks for confirmation messages that should be shown to an interactive user before invoking the operation.   
![Public Method](dotnetimages/publicMethod.gif)| [QueryTransition](topic11192.md)| Queries an transition's tasks for confirmation messages that should be shown to an interactive user before invoking the transition.   
![Public Method](dotnetimages/publicMethod.gif)| [Start](topic11193.md)| Starts a new specification based on the given project.   
![Public Method](dotnetimages/publicMethod.gif)| [UpdateArchivedState](topic11194.md)| Sets the archived state of a loaded/running specification.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AllocateSpecificationId](topic11155.md)| Allocates a specification identifier to the specification, by default, uses the next specification identifier from the group.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertLoaded](topic11156.md)| Raises an exception if the specification context is open.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotLoaded](topic11157.md)| Raises an exception if the specification context is not open.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotRunning](topic11158.md)| Raises an exception if the specification context is in a running state.   
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertRunning](topic11159.md)| Raises an exception if the specification context is not in a running state.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogChanged](topic11178.md)| Raises the [ActiveDialogChanged](topic11237.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogChanging](topic11179.md)| Raises the [ActiveDialogChanging](topic11238.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormChanged](topic11180.md)| Raises the [ActiveDialogOrFormChanged](topic11239.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormChanging](topic11181.md)| Raises the [ActiveDialogOrFormChanging](topic11240.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveDialogOrFormUpdated](topic11182.md)| Raises the [ActiveDialogOrFormUpdated](topic11241.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveFormChanged](topic11183.md)| Raises the [ActiveFormChanged](topic11242.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnActiveFormChanging](topic11184.md)| Raises the [ActiveFormChanging](topic11243.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogClosed](topic11185.md)| Raises the [OnDialogClosed](topic11185.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogClosing](topic11186.md)| Raises the [OnDialogClosing](topic11186.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDialogOpening](topic11187.md)| Raises the [OnDialogOpening](topic11187.md) event.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ActiveDialogChanged](topic11237.md)| Raised when the active dialog changes.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveDialogChanging](topic11238.md)| Raised when the active dialog is about to change.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveDialogOrFormChanged](topic11239.md)| Raised when the active dialog or form changes.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveDialogOrFormChanging](topic11240.md)| Raised when the active dialog or form is about to change.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveDialogOrFormUpdated](topic11241.md)| Raised when the values of one or more controls on the active form or dialog have been changed.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveFormChanged](topic11242.md)| Raised when the active form changes.   
![Public Event](dotnetimages/publicEvent.gif)| [ActiveFormChanging](topic11243.md)| Raised when the active form is about to change.   
![Public Event](dotnetimages/publicEvent.gif)| [AdditionalFoldersCreated](topic11244.md)| Raised when additional folders are created.   
![Public Event](dotnetimages/publicEvent.gif)| [Cancelled](topic11245.md)| Raised when a running state is cancelled.   
![Public Event](dotnetimages/publicEvent.gif)| [ChildContextCreated](topic11246.md)| Raised when a child specification context is created.   
![Public Event](dotnetimages/publicEvent.gif)| [ContextCreatedOnDescendant](topic11247.md)| Raised when a descendant specification context is created. This can be a child or a child's child etc.   
![Public Event](dotnetimages/publicEvent.gif)| [CopiedSpecificationFile](topic11248.md)| Raised after a specification file has successfully been copied to the target location.   
![Public Event](dotnetimages/publicEvent.gif)| [CopyingSpecificationFile](topic11249.md)| Raised before a file for the current specification is copied to its target location.   
![Public Event](dotnetimages/publicEvent.gif)| [CopyRequested](topic11250.md)| Raised when a copy of an existing specification is requested.   
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic11251.md)| Raised when the specification is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [DialogClosed](topic11252.md)| Raised when a dialog has been closed.   
![Public Event](dotnetimages/publicEvent.gif)| [DialogClosing](topic11253.md)| Raised when the active dialog closes.   
![Public Event](dotnetimages/publicEvent.gif)| [DialogOpening](topic11254.md)| Raised when a dialog opens.   
![Public Event](dotnetimages/publicEvent.gif)| [DocumentRegistered](topic11255.md)| Raised when a specification document is registered.   
![Public Event](dotnetimages/publicEvent.gif)| [EventSequenceInvoked](topic11256.md)| Raised when an event task-sequence has been invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [EventSequenceInvoking](topic11257.md)| Raised when an event task-sequence is about to be invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [ForceFormUpdate](topic11258.md)| Raised whenever a manual form update is required.   
![Public Event](dotnetimages/publicEvent.gif)| [FormValueChanged](topic11259.md)| Raised whenever a form value has changed.   
![Public Event](dotnetimages/publicEvent.gif)| [IsLoadedChanged](topic11260.md)| Raised when specification is loaded into/unloaded from the specification context.   
![Public Event](dotnetimages/publicEvent.gif)| [IsRuleProfilingEnabledChanged](topic11261.md)| Raised when the [IsRuleProfilingEnabled](topic11214.md) property changes.   
![Public Event](dotnetimages/publicEvent.gif)| [IsRunningChanged](topic11262.md)| Raised when specification enters or leaves a running state.   
![Public Event](dotnetimages/publicEvent.gif)| [IsRunningChangedOnDescendant](topic11263.md)| Raised when the [IsRunning](topic11215.md) property of a descendent specification context changes. This can be a child or a child's child etc.   
![Public Event](dotnetimages/publicEvent.gif)| [IsRunningChanging](topic11264.md)| Raised when a specification is about to enter or leave a running state.   
![Public Event](dotnetimages/publicEvent.gif)| [OpenRequested](topic11265.md)| Raised when the opening of an existing specification is requested.   
![Public Event](dotnetimages/publicEvent.gif)| [OperationInvoked](topic11266.md)| Raised when a operation has been invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [OperationInvoking](topic11267.md)| Raised when a operation is about to be invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [OperationSequenceInvoked](topic11268.md)| Raised when an operation task-sequence has been invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [OperationSequenceInvoking](topic11269.md)| Raised when an operation task-sequence is about to be invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [ProjectClosing](topic11270.md)| Raised just before the current project is about to be closed, but before saving (which may or may not happen).   
![Public Event](dotnetimages/publicEvent.gif)| [ReportCancelled](topic11271.md)| Raised when the current specification report is cancelled.   
![Public Event](dotnetimages/publicEvent.gif)| [ReportCreated](topic11272.md)| Raised when a specification report is created.   
![Public Event](dotnetimages/publicEvent.gif)| [ReportFinished](topic11273.md)| Raised when the current specification report is finished.   
![Public Event](dotnetimages/publicEvent.gif)| [StartRequested](topic11274.md)| Raised when the start of a new specification is requested.   
![Public Event](dotnetimages/publicEvent.gif)| [StateChanged](topic11275.md)| Raised when a state has been changed.   
![Public Event](dotnetimages/publicEvent.gif)| [StateChanging](topic11276.md)| Raised when a state is about to be changed.   
![Public Event](dotnetimages/publicEvent.gif)| [TaskListEntryAdded](topic11277.md)| Raised when an entry is added to the specification task list.   
![Public Event](dotnetimages/publicEvent.gif)| [TaskListEntryRemoved](topic11278.md)| Raised when an entry is removed from the specification task list.   
![Public Event](dotnetimages/publicEvent.gif)| [TaskListEntryUpdated](topic11279.md)| Raised when an entry in the specification task list is updated.   
![Public Event](dotnetimages/publicEvent.gif)| [TransitionInvoked](topic11280.md)| Raised when a transition has been invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [TransitionInvoking](topic11281.md)| Raised when a transition is about to be invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [TransitionSequenceInvoked](topic11282.md)| Raised when a transition task-sequence has been invoked.   
![Public Event](dotnetimages/publicEvent.gif)| [TransitionSequenceInvoking](topic11283.md)| Raised when a transition task-sequence is about to be invoked.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
