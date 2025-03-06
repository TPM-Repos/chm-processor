![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Extensibility Namespace   
See Also [Inheritance Hierarchy](topic7151.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7150.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.Extensibility Namespace  
---  
  
Glossary Item Box

Provides types related to DriveWorks Engine-level extensibility. 

# ![](dotnetimages/collapse.gif)Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [ComponentTaskConditionNotFoundException](topic7157.md) | Raised when an attempt is made to open a project that contains references to a [DriveWorks.Components.Tasks.ComponentTaskCondition](topic6493.md) or [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md) that are defined in an assembly that is not available.  
![Class](dotnetimages/Class.gif)| [ComponentTaskNotFoundException](topic7167.md) | Raised when an attempt is made to open a project that contains references to [DriveWorks.Components.Tasks.ComponentTask](topic6407.md)s that are defined in an assembly that is not available.  
![Class](dotnetimages/Class.gif)| [ExtensibilityAttribute](topic7177.md) | Provides a base class for all attributes applied to a extension library.  
![Class](dotnetimages/Class.gif)| [FrameworkLibraryAttribute](topic7183.md) | For internal use only. Marks an assembly as being part of the DriveWorks core framework.  
![Class](dotnetimages/Class.gif)| [InvalidPluginAssemblyException](topic7191.md) | Raised when an attempt is made to perform an operation which can only be performed on a extension library.  
![Class](dotnetimages/Class.gif)| [LibraryAttribute](topic7201.md) | Marks an assembly as being a DriveWorks extension library.  
![Class](dotnetimages/Class.gif)| [MacroAttribute](topic7225.md) | Designates a method on a [ProjectExtender](topic7232.md) as a macro.  
![Class](dotnetimages/Class.gif)| [ProjectExtender](topic7232.md) | Provides support for extending a project.  
![Class](dotnetimages/Class.gif)| [SharedProjectExtender](topic7248.md) | Provides support for extending all DriveWorks projects with additional functions.  
![Class](dotnetimages/Class.gif)| [UdfAttribute](topic7256.md) | Designates a method on a [ProjectExtender](topic7232.md) or a [SharedProjectExtender](topic7248.md) as a user defined function to be available in a design master.  
  
# ![](dotnetimages/collapse.gif)Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [IExtension](topic7152.md) | Provides a marker interface which must be implemented by all types which are obtainable from an extension library.  
  
# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


