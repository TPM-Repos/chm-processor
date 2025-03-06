TryGetParameterValueAsInteger Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) : TryGetParameterValueAsInteger Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name as an Integer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetParameterValueAsInteger( _
       ByVal _name_ As String, _
       ByRef _value_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim name As String
    Dim value As Integer
    Dim value As Boolean
     
    value = instance.TryGetParameterValueAsInteger(name, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterValueAsInteger( 
       string _name_ ,
       ref int _value_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_value_
    The calculated value of the parameter if the parameter was found.

#### Return Value

True if the parameter was found and its value could successfully be converted to a Integer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)


