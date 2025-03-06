       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetAccessor Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentTasks Class](topic4163.md) : TryGetAccessor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The unique identifier of the accessor to retrieve.

_accessor_
    The accessor if it was found.

Glossary Item Box

Attempt to get the accessor associated with the specified key. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetAccessor( _
       ByVal _key_ As String, _
       ByRef _accessor_ As [ComponentTaskAccessor](topic6429.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentTasks](topic4163.md)
    Dim key As String
    Dim accessor As [ComponentTaskAccessor](topic6429.md)
    Dim value As Boolean
     
    value = instance.TryGetAccessor(key, accessor)  
  
C#|   
---|---  
      
    
    public bool TryGetAccessor( 
       string _key_ ,
       ref [ComponentTaskAccessor](topic6429.md) _accessor_
    )  
  
#### Parameters

 _key_
    The unique identifier of the accessor to retrieve.
_accessor_
    The accessor if it was found.

#### Return Value

True if the accessor was successfully retrieved.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentTasks Class](topic4163.md)   
[ProjectComponentTasks Members](topic4164.md)


