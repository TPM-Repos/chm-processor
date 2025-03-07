Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueueGarbageCollection Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGarbageCollectionService Interface](topic238.md) : QueueGarbageCollection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Queues a forced garbage collection for the applicaton. If a GC was queued before this will be cancelled so we can GC all in one go. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub QueueGarbageCollection()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGarbageCollectionService](topic238.md)
     
    instance.QueueGarbageCollection()  
  
C#|   
---|---  
      
    
    void QueueGarbageCollection()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGarbageCollectionService Interface](topic238.md)   
[IGarbageCollectionService Members](topic239.md)


