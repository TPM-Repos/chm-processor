Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectInstanceCollection Class](topic14628.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to get.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectInstance](topic14616.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectInstanceCollection](topic14628.md)
    Dim index As Integer
    Dim value As [ProjectInstance](topic14616.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectInstance](topic14616.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the item to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectInstanceCollection Class](topic14628.md)   
[ProjectInstanceCollection Members](topic14629.md)


