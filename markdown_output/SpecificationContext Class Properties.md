       

 Collapse All Expand All  Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationContext Class Properties   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationContext Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [SpecificationContext members](topic11150.md).

# Public Properties

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

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[DriveWorks.Specification Namespace](topic10764.md)


