TryGetParameterValueAsBoolean Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) : TryGetParameterValueAsBoolean Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name as a Boolean. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetParameterValueAsBoolean( _
       ByVal _name_ As String, _
       ByRef _value_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim value As Boolean
    Dim value As Boolean
     
    value = instance.TryGetParameterValueAsBoolean(name, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterValueAsBoolean( 
       string _name_ ,
       ref bool _value_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_value_
    The calculated value of the parameter if the parameter was found.

#### Return Value

True if the parameter was found and it's value could successfully be converted to a Boolean.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)


