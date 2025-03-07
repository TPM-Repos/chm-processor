Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LastProcessedDate Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : LastProcessedDate Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the date we last tried to send the email. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property LastProcessedDate As Nullable(Of Date)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim value As Nullable(Of Date)
     
    instance.LastProcessedDate = value
     
    value = instance.LastProcessedDate  
  
C#|   
---|---  
      
    
    public Nullable<DateTime> LastProcessedDate {get; set;}  
  
#### Property Value

Nothing, if this email was an email created before DriveWorks 12.2 or we've not yet tried to send it, otherwise the date we last tried to send the email.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)


