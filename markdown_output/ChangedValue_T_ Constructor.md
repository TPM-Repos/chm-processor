Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangedValue<T> Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ChangedValue<T> Class](topic2487.md) : ChangedValue<T> Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldValue_
    The old value.

_newValue_
    the new value.

Glossary Item Box

Creates a new instance of the [ChangedValue<T>](topic2487.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _oldValue_ As T, _
       ByVal _newValue_ As T _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim oldValue As T
    Dim newValue As T
     
    Dim instance As New [ChangedValue(Of T)](topic2487.md)(oldValue, newValue)  
  
C#|   
---|---  
      
    
    public ChangedValue<T>( 
       T _oldValue_ ,
       T _newValue_
    )  
  
#### Parameters

 _oldValue_
    The old value.
_newValue_
    the new value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ChangedValue<T> Class](topic2487.md)   
[ChangedValue<T> Members](topic2488.md)


