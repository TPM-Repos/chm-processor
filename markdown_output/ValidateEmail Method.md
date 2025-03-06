ValidateEmail Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateEmail Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_email_
    The name to validate.

Glossary Item Box

Validates an email address. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateEmail( _
       ByVal _email_ As String _
    ) As [ValidateEmailResult](topic13192.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim email As String
    Dim value As [ValidateEmailResult](topic13192.md)
     
    value = [ValidationUtility](topic13287.md).ValidateEmail(email)  
  
C#|   
---|---  
      
    
    public static [ValidateEmailResult](topic13192.md) ValidateEmail( 
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


