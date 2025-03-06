TryGetParameterValueAsDouble Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) : TryGetParameterValueAsDouble Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name as a Double. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetParameterValueAsDouble( _
       ByVal _name_ As String, _
       ByRef _value_ As Double _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim value As Double
    Dim value As Boolean
     
    value = instance.TryGetParameterValueAsDouble(name, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterValueAsDouble( 
       string _name_ ,
       ref double _value_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_value_
    The calculated value of the parameter if the parameter was found.

#### Return Value

True if the parameter was found and it's value could successfully be converted to a Double.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)


