TryGetParameterAsArrayValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) : TryGetParameterAsArrayValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name as a **Titan.Rules.Execution.IArrayValue**. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetParameterAsArrayValue( _
       ByVal _name_ As String, _
       ByRef _value_ As Titan.Rules.Execution.IArrayValue _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim name As String
    Dim value As Titan.Rules.Execution.IArrayValue
    Dim value As Boolean
     
    value = instance.TryGetParameterAsArrayValue(name, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterAsArrayValue( 
       string _name_ ,
       ref Titan.Rules.Execution.IArrayValue _value_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_value_
    The calculated value of the parameter if the parameter was found.

#### Return Value

True if the parameter was found and its value could successfully be converted to a **Titan.Rules.Execution.IArrayValue**

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)


