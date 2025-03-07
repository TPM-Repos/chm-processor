Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetParameterValue(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) > [GetParameterValue Method](topic5067.md) : GetParameterValue(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose value to retrieve.

_fallbackValue_
    The value to return if the parameter could not be found.

Glossary Item Box

Gets the value of the parameter with the given name as a string, or the fallback value if the parameter could not be found, or has no value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetParameterValue( _
       ByVal _name_ As String, _
       ByVal _fallbackValue_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim name As String
    Dim fallbackValue As String
    Dim value As String
     
    value = instance.GetParameterValue(name, fallbackValue)  
  
C#|   
---|---  
      
    
    public string GetParameterValue( 
       string _name_ ,
       string _fallbackValue_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose value to retrieve.
_fallbackValue_
    The value to return if the parameter could not be found.

#### Return Value

The value of the parameter, or the fallback value if it wasn't found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)   
[Overload List](topic5067.md)


