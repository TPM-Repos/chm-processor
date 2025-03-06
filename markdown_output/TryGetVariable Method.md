       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetVariable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariables Class](topic5010.md) : TryGetVariable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the variable to retrieve.

_variable_
    A reference to a variable which will receive the variable.

Glossary Item Box

Gets the variable with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function TryGetVariable( _
       ByVal _displayName_ As String, _
       ByRef _variable_ As [ProjectVariable](topic4927.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariables](topic5010.md)
    Dim displayName As String
    Dim variable As [ProjectVariable](topic4927.md)
    Dim value As Boolean
     
    value = instance.TryGetVariable(displayName, variable)  
  
C#|   
---|---  
      
    
    public abstract bool TryGetVariable( 
       string _displayName_ ,
       ref [ProjectVariable](topic4927.md) _variable_
    )  
  
#### Parameters

 _displayName_
    The display name of the variable to retrieve.
_variable_
    A reference to a variable which will receive the variable.

#### Return Value

True if the variable is found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariables Class](topic5010.md)   
[ProjectVariables Members](topic5011.md)


