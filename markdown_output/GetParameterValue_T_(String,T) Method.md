_T_
    The type of the parameter to retrieve.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetParameterValue<T>(String,T) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) > [GetParameterValue Method](topic5067.md) : GetParameterValue<T>(String,T) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose value to retrieve.

_fallbackValue_
    The value to return if the parameter could not be found.

Glossary Item Box

Retrieves the value of the parameter with the given name, or fallbackValue if it wasn't found. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetParameterValue(Of T As {New, Struct})( _
       ByVal _name_ As String, _
       ByVal _fallbackValue_ As T _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim name As String
    Dim fallbackValue As T
    Dim value As T
     
    value = instance.GetParameterValue(Of T)(name, fallbackValue)  
  
C#|   
---|---  
      
    
    public T GetParameterValue<T>( 
       string _name_ ,
       T _fallbackValue_
    )
    where T: new(), struct  
  
#### Parameters

 _name_
    The name of the parameter whose value to retrieve.
_fallbackValue_
    The value to return if the parameter could not be found.

#### Type Parameters

_T_
    The type of the parameter to retrieve.

#### Return Value

The value of the parameter, or the fallback value if it wasn't found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)   
[Overload List](topic5067.md)


