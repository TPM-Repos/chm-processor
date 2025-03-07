Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the step to get.

Glossary Item Box

Gets the navigation step at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [NavigationStep](topic10175.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim index As Integer
    Dim value As [NavigationStep](topic10175.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [NavigationStep](topic10175.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the step to get.

#### Property Value

A navigation step.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


