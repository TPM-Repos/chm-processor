Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateVariable(String,String,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateVariable Method](topic13074.md) : CreateTxCreateVariable(String,String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the variable to create.

_rule_
    The rule to apply, or a null reference to not apply a comment..

_comment_
    The comment to apply, or a null reference to not apply a comment.

_category_
    The category by its path to apply, or a null reference to not apply a category.

Glossary Item Box

Creates a transaction which, when committed, will create a new variable. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateVariable( _
       ByVal _displayName_ As String, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String, _
       ByVal _category_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim displayName As String
    Dim rule As String
    Dim comment As String
    Dim category As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateVariable(displayName, rule, comment, category)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateVariable( 
       string _displayName_ ,
       string _rule_ ,
       string _comment_ ,
       string _category_
    )  
  
#### Parameters

 _displayName_
    The display name of the variable to create.
_rule_
    The rule to apply, or a null reference to not apply a comment..
_comment_
    The comment to apply, or a null reference to not apply a comment.
_category_
    The category by its path to apply, or a null reference to not apply a category.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13074.md)


