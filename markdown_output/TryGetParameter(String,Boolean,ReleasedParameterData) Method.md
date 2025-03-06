TryGetParameter(String,Boolean,ReleasedParameterData) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) > [TryGetParameter Method](topic5070.md) : TryGetParameter(String,Boolean,ReleasedParameterData) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter to get.

_excludeEmpty_
    True if an empty parameter value should be considered non-existent.

_parameter_
    The parameter if it was found.

Glossary Item Box

Attempts to get the paramter data that matches the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetParameter( _
       ByVal _name_ As String, _
       ByVal _excludeEmpty_ As Boolean, _
       ByRef _parameter_ As ReleasedParameterData _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim name As String
    Dim excludeEmpty As Boolean
    Dim parameter As ReleasedParameterData
    Dim value As Boolean
     
    value = instance.TryGetParameter(name, excludeEmpty, parameter)  
  
C#|   
---|---  
      
    
    public bool TryGetParameter( 
       string _name_ ,
       bool _excludeEmpty_ ,
       ref ReleasedParameterData _parameter_
    )  
  
#### Parameters

 _name_
    The name of the parameter to get.
_excludeEmpty_
    True if an empty parameter value should be considered non-existent.
_parameter_
    The parameter if it was found.

#### Return Value

True if the parameter was found. If excludeEmpty is True then returns whether the parameter was found and it's value was not empty.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)   
[Overload List](topic5070.md)


