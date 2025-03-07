Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateVariable(String,ProjectVariableCategory,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariables Class](topic5010.md) > [CreateVariable Method](topic5016.md) : CreateVariable(String,ProjectVariableCategory,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The name of the new variable.

_category_
    The parent category, or a null reference (Nothing in Visual Basic) to leave the variable without a parent category.

_rule_
    The initial rule to assign to the variable.

_comment_
    The initial comment to assign to the variable.

Glossary Item Box

Creates a new variable with the specified name in the given category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads MustOverride Function CreateVariable( _
       ByVal _displayName_ As String, _
       ByVal _category_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _rule_ As String, _
       ByVal _comment_ As String _
    ) As [ProjectVariable](topic4927.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariables](topic5010.md)
    Dim displayName As String
    Dim category As [ProjectVariableCategory](topic4983.md)
    Dim rule As String
    Dim comment As String
    Dim value As [ProjectVariable](topic4927.md)
     
    value = instance.CreateVariable(displayName, category, rule, comment)  
  
C#|   
---|---  
      
    
    public abstract [ProjectVariable](topic4927.md) CreateVariable( 
       string _displayName_ ,
       [ProjectVariableCategory](topic4983.md) _category_ ,
       string _rule_ ,
       string _comment_
    )  
  
#### Parameters

 _displayName_
    The name of the new variable.
_category_
    The parent category, or a null reference (Nothing in Visual Basic) to leave the variable without a parent category.
_rule_
    The initial rule to assign to the variable.
_comment_
    The initial comment to assign to the variable.

#### Return Value

The newly created variable.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariables Class](topic5010.md)   
[ProjectVariables Members](topic5011.md)   
[Overload List](topic5016.md)


