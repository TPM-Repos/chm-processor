ValueChangedEventArgs Constructor(DynamicProperty,Object,Object)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [ValueChangedEventArgs Class](topic9575.md) > [ValueChangedEventArgs Constructor](topic9581.md) : ValueChangedEventArgs Constructor(DynamicProperty,Object,Object)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dp_
    The property which has changed.

_oldValue_
    The value of the property before it was changed.

_newValue_
    The value of the property after it was changed.

Glossary Item Box

Initializes a new instance of the [ValueChangedEventArgs](topic9575.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _dp_ As [DynamicProperty](topic9398.md), _
       ByVal _oldValue_ As Object, _
       ByVal _newValue_ As Object _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim dp As [DynamicProperty](topic9398.md)
    Dim oldValue As Object
    Dim newValue As Object
     
    Dim instance As New [ValueChangedEventArgs](topic9575.md)(dp, oldValue, newValue)  
  
C#|   
---|---  
      
    
    public ValueChangedEventArgs( 
       [DynamicProperty](topic9398.md) _dp_ ,
       object _oldValue_ ,
       object _newValue_
    )  
  
#### Parameters

 _dp_
    The property which has changed.
_oldValue_
    The value of the property before it was changed.
_newValue_
    The value of the property after it was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValueChangedEventArgs Class](topic9575.md)   
[ValueChangedEventArgs Members](topic9576.md)   
[Overload List](topic9581.md)


