WindowsAccountNameUsed Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlTestResult Class](topic5450.md) : WindowsAccountNameUsed Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

If a windows account was used to connect to the server then this is the full name of that account. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property WindowsAccountNameUsed As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlTestResult](topic5450.md)
    Dim value As String
     
    instance.WindowsAccountNameUsed = value
     
    value = instance.WindowsAccountNameUsed  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string WindowsAccountNameUsed {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlTestResult Class](topic5450.md)   
[SqlTestResult Members](topic5451.md)


