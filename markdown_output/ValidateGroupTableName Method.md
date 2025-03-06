ValidateGroupTableName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateGroupTableName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name to validate.

Glossary Item Box

Validates a DriveWorks group table name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateGroupTableName( _
       ByVal _tableName_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim tableName As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateGroupTableName(tableName)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateGroupTableName( 
       string _tableName_
    )  
  
#### Parameters

 _tableName_
    The name to validate.

#### Return Value

The result of the validation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


