ValidateUserEmail Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateUserEmail Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_email_
    The name to validate.

Glossary Item Box

Validates a DriveWorks user email. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateUserEmail( _
       ByVal _email_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim email As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateUserEmail(email)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateUserEmail( 
       string _email_
    )  
  
#### Parameters

 _email_
    The name to validate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


