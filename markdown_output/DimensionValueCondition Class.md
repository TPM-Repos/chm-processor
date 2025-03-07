Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DimensionValueCondition Class   
[Members](topic13537.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : DimensionValueCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Object Model

![](dotnetdiagramimages/image733.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[GenerationTaskConditionAttribute](topic13721.md)(Scope=GenerationTaskScope.Assemblies Or  _
        GenerationTaskScope.Parts Or  _
        GenerationTaskScope.Drawings Or  _
        GenerationTaskScope.All, 
       Title="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DimValueConditionName", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DimValueConditionDescription", 
       Image="embedded://DriveWorks.SolidWorks.DimensionPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.Before Or  _
        ComponentTaskSequenceLocation.After Or  _
        ComponentTaskSequenceLocation.PreClose)>
    Public Class DimensionValueCondition 
       Inherits [GenerationTaskCondition](topic13707.md)
       Implements [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DimensionValueCondition](topic13536.md)  
  
C#|   
---|---  
      
    
    [[GenerationTaskConditionAttribute](topic13721.md)(Scope=GenerationTaskScope.Assemblies | 
        GenerationTaskScope.Parts | 
        GenerationTaskScope.Drawings | 
        GenerationTaskScope.All, 
       Title="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DimValueConditionName", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,DimValueConditionDescription", 
       Image="embedded://DriveWorks.SolidWorks.DimensionPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.Before | 
        ComponentTaskSequenceLocation.After | 
        ComponentTaskSequenceLocation.PreClose)]
    public class DimensionValueCondition : [GenerationTaskCondition](topic13707.md), [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.SolidWorks.GenerationTaskCondition](topic13707.md)  
**DriveWorks.SolidWorks.DimensionValueCondition**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DimensionValueCondition Members](topic13537.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


