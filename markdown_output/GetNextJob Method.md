Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNextJob Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobQueue Class](topic3594.md) : GetNextJob Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tagInformation_
    The tag information for this job request.

Glossary Item Box

Gets the next job in the queue. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetNextJob( _
       ByVal _tagInformation_ As [JobRequestTagInformation](topic3604.md) _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JobQueue](topic3594.md)
    Dim tagInformation As [JobRequestTagInformation](topic3604.md)
    Dim value As Object
     
    value = instance.GetNextJob(tagInformation)  
  
C#|   
---|---  
      
    
    public object GetNextJob( 
       [JobRequestTagInformation](topic3604.md) _tagInformation_
    )  
  
#### Parameters

 _tagInformation_
    The tag information for this job request.

#### Return Value

The next job to process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobQueue Class](topic3594.md)   
[JobQueue Members](topic3595.md)


