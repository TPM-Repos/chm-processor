TryGetParameter Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFormat Class](topic14925.md) : TryGetParameter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the parameter to get.

_parameter_
    The a reference for the matching parameter.

Glossary Item Box

Attempts to get the parameter data that matches the specified address. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetParameter( _
       ByVal _address_ As String, _
       ByRef _parameter_ As ReleasedParameterData _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFormat](topic14925.md)
    Dim address As String
    Dim parameter As ReleasedParameterData
    Dim value As Boolean
     
    value = instance.TryGetParameter(address, parameter)  
  
C#|   
---|---  
      
    
    public bool TryGetParameter( 
       string _address_ ,
       ref ReleasedParameterData _parameter_
    )  
  
#### Parameters

 _address_
    The address of the parameter to get.
_parameter_
    The a reference for the matching parameter.

#### Return Value

True if an match was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFormat Class](topic14925.md)   
[ReleasedFormat Members](topic14926.md)


