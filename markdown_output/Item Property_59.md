Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskCollection Class](topic6466.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskCollection](topic6466.md)
    Dim index As Integer
    Dim value As [ComponentTask](topic6407.md)
     
    instance.Item(index) = value
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) this[ 
       int _index_
    ]; {get; set;}  
  
#### Parameters

 _index_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskCollection Class](topic6466.md)   
[ComponentTaskCollection Members](topic6467.md)


