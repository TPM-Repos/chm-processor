Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVariable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariables Class](topic5010.md) : GetVariable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the variable to retrieve.

Glossary Item Box

Gets the variable with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetVariable( _
       ByVal _displayName_ As String _
    ) As [ProjectVariable](topic4927.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariables](topic5010.md)
    Dim displayName As String
    Dim value As [ProjectVariable](topic4927.md)
     
    value = instance.GetVariable(displayName)  
  
C#|   
---|---  
      
    
    public abstract [ProjectVariable](topic4927.md) GetVariable( 
       string _displayName_
    )  
  
#### Parameters

 _displayName_
    The display name of the variable to retrieve.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown when no variable with the specified display name exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariables Class](topic5010.md)   
[ProjectVariables Members](topic5011.md)


