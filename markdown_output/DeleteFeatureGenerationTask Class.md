![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteFeatureGenerationTask Class   
[Members](topic15310.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15309.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks Namespace](topic15301.md) : DeleteFeatureGenerationTask Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image874.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[GenerationTaskAttribute](topic13693.md)(Scope=GenerationTaskScope.Assemblies Or  _
        GenerationTaskScope.Parts, 
       Name="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeatureTaskTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeatureTaskDescription", 
       Image="embedded://DriveWorks.SolidWorks.DeleteFeaturePlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryPartsAndAssemblies", 
       AllowedLocations=ComponentTaskSequenceLocation.Before Or  _
        ComponentTaskSequenceLocation.After)>
    Public Class DeleteFeatureGenerationTask 
       Inherits [DriveWorks.SolidWorks.GenerationTask](topic13678.md)
       Implements [DriveWorks.Components.Tasks.IComponentTask](topic6393.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DeleteFeatureGenerationTask](topic15309.md)  
  
C#|   
---|---  
      
    
    [[GenerationTaskAttribute](topic13693.md)(Scope=GenerationTaskScope.Assemblies | 
        GenerationTaskScope.Parts, 
       Name="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeatureTaskTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DeleteFeatureTaskDescription", 
       Image="embedded://DriveWorks.SolidWorks.DeleteFeaturePlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryPartsAndAssemblies", 
       AllowedLocations=ComponentTaskSequenceLocation.Before | 
        ComponentTaskSequenceLocation.After)]
    public class DeleteFeatureGenerationTask : [DriveWorks.SolidWorks.GenerationTask](topic13678.md), [DriveWorks.Components.Tasks.IComponentTask](topic6393.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
[DriveWorks.SolidWorks.GenerationTask](topic13678.md)  
**DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks.DeleteFeatureGenerationTask**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DeleteFeatureGenerationTask Members](topic15310.md)   
[DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks Namespace](topic15301.md)

©2024 DriveWorks Ltd. All Rights Reserved.
