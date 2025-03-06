TryGetProperty Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) : TryGetProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_propertyName_
    The name of the property to get.

_result_
    Receives the property with the given name.

Glossary Item Box

Tries to get a specification property with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetProperty( _
       ByVal _propertyName_ As String, _
       ByRef _result_ As [ProjectSpecificationProperty](topic4853.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim propertyName As String
    Dim result As [ProjectSpecificationProperty](topic4853.md)
    Dim value As Boolean
     
    value = instance.TryGetProperty(propertyName, result)  
  
C#|   
---|---  
      
    
    public bool TryGetProperty( 
       string _propertyName_ ,
       ref [ProjectSpecificationProperty](topic4853.md) _result_
    )  
  
#### Parameters

 _propertyName_
    The name of the property to get.
_result_
    Receives the property with the given name.

#### Return Value

True if the property is found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)


