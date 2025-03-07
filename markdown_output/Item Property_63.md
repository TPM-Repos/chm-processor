Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskRuleCollection Class](topic6723.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ComponentTaskProperty](topic6633.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskRuleCollection](topic6723.md)
    Dim index As Integer
    Dim value As [ComponentTaskProperty](topic6633.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ComponentTaskProperty](topic6633.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskRuleCollection Class](topic6723.md)   
[ComponentTaskRuleCollection Members](topic6724.md)


