Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : Load Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_group_
    A group from which to load group settings, or a null reference to not load settings from a group.

_settingsManager_
    A settings manager from which to load other settings, or a null reference to not load settings from a settings manager.

Glossary Item Box

Loads settings from the specified group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Load( _
       ByVal _group_ As [Group](topic2958.md), _
       ByVal _settingsManager_ As [ISettingsManager](topic442.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim group As [Group](topic2958.md)
    Dim settingsManager As [ISettingsManager](topic442.md)
     
    instance.Load(group, settingsManager)  
  
C#|   
---|---  
      
    
    public void Load( 
       [Group](topic2958.md) _group_ ,
       [ISettingsManager](topic442.md) _settingsManager_
    )  
  
#### Parameters

 _group_
    A group from which to load group settings, or a null reference to not load settings from a group.
_settingsManager_
    A settings manager from which to load other settings, or a null reference to not load settings from a settings manager.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


