       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValueChangedEventArgs<T> Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ValueChangedEventArgs<T> Class](topic5834.md) : ValueChangedEventArgs<T> Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldValue_
    The previous value for the item that has changed.

_newValue_
    The new value for the item that has changed.

Glossary Item Box

Creates a new instance of the [ValueChangedEventArgs<T>](topic5834.md) class. 

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
     
    Dim instance As New [ValueChangedEventArgs(Of T)](topic5834.md)(oldValue, newValue)  
  
C#|   
---|---  
      
    
    public ValueChangedEventArgs<T>( 
       T _oldValue_ ,
       T _newValue_
    )  
  
#### Parameters

 _oldValue_
    The previous value for the item that has changed.
_newValue_
    The new value for the item that has changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValueChangedEventArgs<T> Class](topic5834.md)   
[ValueChangedEventArgs<T> Members](topic5835.md)


