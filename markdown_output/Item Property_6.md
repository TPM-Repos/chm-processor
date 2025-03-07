Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The zero-based index of the task to retrieve.

Glossary Item Box

Gets the task at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [Task](topic11629.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim index As Integer
    Dim value As [Task](topic11629.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [Task](topic11629.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The zero-based index of the task to retrieve.

# Exceptions

Exception| Description  
---|---  
System.IndexOutOfRangeException| Thrown if the specified index is out of range.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)


