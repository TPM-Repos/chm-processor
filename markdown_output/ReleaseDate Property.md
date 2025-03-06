ReleaseDate Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : ReleaseDate Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the date the email was released. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ReleaseDate As Nullable(Of Date)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim value As Nullable(Of Date)
     
    instance.ReleaseDate = value
     
    value = instance.ReleaseDate  
  
C#|   
---|---  
      
    
    public Nullable<DateTime> ReleaseDate {get; set;}  
  
#### Property Value

Nothing, if this was an email created before DriveWorks 12.2, otherwise the date the email was released.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)


