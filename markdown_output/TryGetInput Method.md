TryGetInput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : TryGetInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantName_
    Name of the constant to get the input for.

_input_
    The input to be set.

Glossary Item Box

Attempts to get a specified input from the given constant name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetInput( _
       ByVal _constantName_ As String, _
       ByRef _input_ As [ProjectChildSpecificationInputDef](topic4047.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim constantName As String
    Dim input As [ProjectChildSpecificationInputDef](topic4047.md)
    Dim value As Boolean
     
    value = instance.TryGetInput(constantName, input)  
  
C#|   
---|---  
      
    
    public bool TryGetInput( 
       string _constantName_ ,
       ref [ProjectChildSpecificationInputDef](topic4047.md) _input_
    )  
  
#### Parameters

 _constantName_
    Name of the constant to get the input for.
_input_
    The input to be set.

#### Return Value

True if the input was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)


