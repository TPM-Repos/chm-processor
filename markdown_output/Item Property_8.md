Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transitions Class](topic11787.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The zero-based index of the transition to get.

Glossary Item Box

Gets the transition at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [Transition](topic11757.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Transitions](topic11787.md)
    Dim index As Integer
    Dim value As [Transition](topic11757.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [Transition](topic11757.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The zero-based index of the transition to get.

#### Property Value

The transition at the specified index.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Transitions Class](topic11787.md)   
[Transitions Members](topic11788.md)


