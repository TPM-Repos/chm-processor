Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConstant Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) : GetConstant Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the constant to retrieve.

Glossary Item Box

Gets the constant with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetConstant( _
       ByVal _displayName_ As String _
    ) As [ProjectConstant](topic4171.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim displayName As String
    Dim value As [ProjectConstant](topic4171.md)
     
    value = instance.GetConstant(displayName)  
  
C#|   
---|---  
      
    
    public abstract [ProjectConstant](topic4171.md) GetConstant( 
       string _displayName_
    )  
  
#### Parameters

 _displayName_
    The display name of the constant to retrieve.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown when no constant with the specified display name exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)


