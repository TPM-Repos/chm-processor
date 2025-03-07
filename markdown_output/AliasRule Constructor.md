Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AliasRule Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [AliasRule Class](topic6001.md) : AliasRule Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to create an alias for.

_displayName_
    The display name to show.

Glossary Item Box

Creates a new instance of the [AliasRule](topic6001.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _rule_ As [IHasRule](topic5947.md), _
       ByVal _displayName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim rule As [IHasRule](topic5947.md)
    Dim displayName As String
     
    Dim instance As New [AliasRule](topic6001.md)(rule, displayName)  
  
C#|   
---|---  
      
    
    public AliasRule( 
       [IHasRule](topic5947.md) _rule_ ,
       string _displayName_
    )  
  
#### Parameters

 _rule_
    The rule to create an alias for.
_displayName_
    The display name to show.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AliasRule Class](topic6001.md)   
[AliasRule Members](topic6002.md)


