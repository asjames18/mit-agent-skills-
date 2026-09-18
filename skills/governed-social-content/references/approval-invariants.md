# Approval Invariants

Read this reference whenever the requested workflow reaches approval, scheduling, publishing, replying, commenting, messaging, or another account-affecting action.

## Exact-match requirement

An approval is valid only when it matches the proposed action's:

- Content item ID
- Revision ID
- Cryptographic content hash
- Platform and channel account ID
- Action type
- Media IDs or immutable media hashes
- Thread or carousel ordering
- Reply or comment target, when applicable

The approval must be explicitly `approved`, unexpired, unrevoked, and unconsumed.

Any edit to copy, media, order, target, account, or action creates a new revision and invalidates the previous approval. Scheduling does not imply approval. Approval does not imply immediate execution.

## Safe execution

Unless a separate publishing workflow is explicitly authorized, stop at an approval-ready packet.

When execution is authorized:

1. Revalidate the exact revision and all approval fields immediately before the action.
2. Show the exact action-ready content and target to the user when action-time confirmation is required.
3. Use idempotency and an audit record so retries cannot duplicate a post or create a partial thread.
4. Stop on any mismatch, expired approval, ambiguous result, partial failure, or changed external state.
5. Never silently retry an uncertain public action.

The initial safe scope is drafting and approval preparation. Likes, reactions, follows, connections, reposts, profile edits, deletions, and direct messages require their own explicit authority and should not be inferred from approval to publish a post.
