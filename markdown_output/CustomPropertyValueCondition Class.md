Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CustomPropertyValueCondition Class   
[Members](topic13528.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : CustomPropertyValueCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Object Model

![](dotnetdiagramimages/image732.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[GenerationTaskConditionAttribute](topic13721.md)(Scope=GenerationTaskScope.Assemblies Or  _
        GenerationTaskScope.Parts Or  _
        GenerationTaskScope.Drawings Or  _
        GenerationTaskScope.All, 
       Title="resx://DriveWorks.SolidWorks.TasksLocalizedResources,CPValueConditionTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,CPValueConditionDescription", 
       Image="embedded://DriveWorks.SolidWorks.CustomPropertiesPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.Before Or  _
        ComponentTaskSequenceLocation.After Or  _
        ComponentTaskSequenceLocation.PreClose)>
    Public Class CustomPropertyValueCondition 
       Inherits [GenerationTaskCondition](topic13707.md)
       Implements [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CustomPropertyValueCondition](topic13527.md)  
  
C#|   
---|---  
      
    
    [[GenerationTaskConditionAttribute](topic13721.md)(Scope=GenerationTaskScope.Assemblies | 
        GenerationTaskScope.Parts | 
        GenerationTaskScope.Drawings | 
        GenerationTaskScope.All, 
       Title="resx://DriveWorks.SolidWorks.TasksLocalizedResources,CPValueConditionTitle", 
       Description="resx://DriveWorks.SolidWorks.TasksLocalizedResources,CPValueConditionDescription", 
       Image="embedded://DriveWorks.SolidWorks.CustomPropertiesPlain16.png", 
       Category="resx://DriveWorks.SolidWorks.TasksLocalizedResources,TaskCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.Before | 
        ComponentTaskSequenceLocation.After | 
        ComponentTaskSequenceLocation.PreClose)]
    public class CustomPropertyValueCondition : [GenerationTaskCondition](topic13707.md), [DriveWorks.Components.Tasks.IComponentTaskCondition](topic6399.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.SolidWorks.GenerationTaskCondition](topic13707.md)  
**DriveWorks.SolidWorks.CustomPropertyValueCondition**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CustomPropertyValueCondition Members](topic13528.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


