Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PostCloseFailed Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : PostCloseFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the Post Close sequence execution fails. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PostCloseFailed As EventHandler(Of ExceptionEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler(Of ExceptionEventArgs)
     
    AddHandler instance.PostCloseFailed, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ExceptionEventArgs> PostCloseFailed  
  
# Event Data

The event handler receives an argument of type [ExceptionEventArgs](topic806.md) containing data related to this event. The following **ExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic813.md)| Gets the exception to which the event refers.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


