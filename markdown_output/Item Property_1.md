Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The zero-based index of the condition to get.

Glossary Item Box

Gets the condition at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [Condition](topic10804.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim index As Integer
    Dim value As [Condition](topic10804.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [Condition](topic10804.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The zero-based index of the condition to get.

# Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Thrown if the specified index is out of range.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)


