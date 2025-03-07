Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteFeaturesGenerationTask Class   
[Members](topic15319.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks Namespace](topic15301.md) : DeleteFeaturesGenerationTask Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Object Model

![](dotnetdiagramimages/image875.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[GenerationTaskAttribute](topic13693.md)(Scope=GenerationTaskScope.Assemblies Or  _
        GenerationTaskScope.Parts, 
       Name="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeaturesTaskTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeaturesTaskDescription", 
       Image="embedded://DriveWorks.SolidWorks.DeleteFeaturesPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryPartsAndAssemblies", 
       AllowedLocations=ComponentTaskSequenceLocation.Before Or  _
        ComponentTaskSequenceLocation.After)>
    Public Class DeleteFeaturesGenerationTask 
       Inherits [DriveWorks.SolidWorks.GenerationTask](topic13678.md)
       Implements [DriveWorks.Components.Tasks.IComponentTask](topic6393.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeleteFeaturesGenerationTask](topic15318.md)  
  
C#|   
---|---  
      
    
    [[GenerationTaskAttribute](topic13693.md)(Scope=GenerationTaskScope.Assemblies | 
        GenerationTaskScope.Parts, 
       Name="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeaturesTaskTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeaturesTaskDescription", 
       Image="embedded://DriveWorks.SolidWorks.DeleteFeaturesPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryPartsAndAssemblies", 
       AllowedLocations=ComponentTaskSequenceLocation.Before | 
        ComponentTaskSequenceLocation.After)]
    public class DeleteFeaturesGenerationTask : [DriveWorks.SolidWorks.GenerationTask](topic13678.md), [DriveWorks.Components.Tasks.IComponentTask](topic6393.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.SolidWorks.GenerationTask](topic13678.md)  
**DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks.DeleteFeaturesGenerationTask**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DeleteFeaturesGenerationTask Members](topic15319.md)   
[DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks Namespace](topic15301.md)


