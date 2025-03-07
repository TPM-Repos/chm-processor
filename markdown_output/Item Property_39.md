Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectViewCollection Class](topic14719.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the view to get.

Glossary Item Box

Gets the view at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectView](topic14703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectViewCollection](topic14719.md)
    Dim index As Integer
    Dim value As [ProjectView](topic14703.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectView](topic14703.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the view to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectViewCollection Class](topic14719.md)   
[ProjectViewCollection Members](topic14720.md)


