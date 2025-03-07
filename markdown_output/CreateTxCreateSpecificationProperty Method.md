Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateSpecificationProperty Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateSpecificationProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give the new property.

_rule_
    The rule to apply to the new property.

_comment_
    The comment to apply to the new property.

_index_
    The index to insert the property at, any invalid index will result in the property being appended on the list.

Glossary Item Box

Creates a transaction which, when commited, will create a new specification property with the given values. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateSpecificationProperty( _
       ByVal _name_ As String, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String, _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim name As String
    Dim rule As String
    Dim comment As String
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateSpecificationProperty(name, rule, comment, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateSpecificationProperty( 
       string _name_ ,
       string _rule_ ,
       string _comment_ ,
       int _index_
    )  
  
#### Parameters

 _name_
    The name to give the new property.
_rule_
    The rule to apply to the new property.
_comment_
    The comment to apply to the new property.
_index_
    The index to insert the property at, any invalid index will result in the property being appended on the list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


